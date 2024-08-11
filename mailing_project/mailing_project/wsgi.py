from django.core.wsgi import get_wsgi_application
from mailing_project import settings
from mailings.tasks import start_scheduler

application = get_wsgi_application()

if settings.DEBUG:
    start_scheduler()
