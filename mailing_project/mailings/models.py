from django.db import models

class Mailing(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    send_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('sent', 'Sent')])
    recipients = models.TextField(help_text="Enter comma-separated list of email addresses")

    def __str__(self):
        return self.title
