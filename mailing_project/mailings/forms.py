from django import forms
from .models import Client, Message, Mailing, MailingAttempt

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['first_send_date', 'periodicity', 'status', 'message', 'clients']

class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ['mailing', 'status', 'server_response']
