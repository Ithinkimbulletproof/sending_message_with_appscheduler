from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailings.models import Mailing
from django.utils import timezone


class Command(BaseCommand):
    help = "Send pending mailings"

    def handle(self, *args, **kwargs):
        mailings = Mailing.objects.filter(
            send_time__lte=timezone.now(), status="pending"
        )
        for mailing in mailings:
            recipients = mailing.recipients.split(",")
            for recipient in recipients:
                send_mail(
                    subject=mailing.title,
                    message=mailing.message,
                    from_email="your_email@example.com",
                    recipient_list=[recipient],
                    fail_silently=False,
                )
            mailing.status = "sent"
            mailing.save()
        self.stdout.write(self.style.SUCCESS("Successfully sent all pending mailings"))
