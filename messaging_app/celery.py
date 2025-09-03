# celery.py
import os
from celery import Celery

# set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messaging_app.settings")

app = Celery("messaging_app")

# Load settings from Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in installed apps
app.autodiscover_tasks()
