# mailings/tasks.py

from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from django.core.mail import send_mail
from .models import Mailing


def send_mailings():
    mailings = Mailing.objects.filter(send_time__lte=timezone.now(), status="pending")
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


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, "interval", minutes=60)
    scheduler.start()
