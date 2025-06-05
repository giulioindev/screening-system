import os
from uuid import UUID

from kombu.utils.json import register_type

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
register_type(UUID, "uuid", str, UUID)
