from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class MailingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailings"

    def ready(self):
        from .tasks import start_scheduler

        start_scheduler()
