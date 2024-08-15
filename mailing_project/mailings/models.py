from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse

CREATE = "Создана"
IN_WORK = "В работе"
DONE = "Завершена"
ERROR = "Ошибка отправки"

DAILY = "раз в день"
WEEKLY = "раз в неделю"
MONTHLY = "раз в месяц"

FREQUENCY_CHOICES = [
    (DAILY, "Ежедневно"),
    (WEEKLY, "Еженедельно"),
    (MONTHLY, "Ежемесячно"),
]
STATUS_OF_NEWSLETTER = [
    (CREATE, "Создана"),
    (IN_WORK, "В работе"),
    (DONE, "Завершена"),
    (ERROR, "Ошибка отправки"),
]


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('mailings:client_detail', kwargs={'pk': self.pk})


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    PERIODICITY_CHOICES = [
        ("daily", "Раз в день"),
        ("weekly", "Раз в неделю"),
        ("monthly", "Раз в месяц"),
    ]

    first_send_date = models.DateTimeField(default=timezone.now)
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=[
            ("created", "Создана"),
            ("started", "Запущена"),
            ("completed", "Завершена"),
        ],
        default="created",
    )
    is_active = models.BooleanField(default=True)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Mailing {self.id} - {self.status}"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ("success", "Успешно"),
        ("failure", "Неуспешно"),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"
