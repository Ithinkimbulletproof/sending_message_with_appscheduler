from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number', 'comment')
    fields = ('email', 'full_name', 'phone_number', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "body")


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("first_send_date", "periodicity", "status")


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("mailing", "attempt_date", "status", "server_response")
