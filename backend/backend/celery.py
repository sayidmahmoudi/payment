import os

from datetime import timedelta
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.result_expires = 180


app.conf.beat_schedule = {
    'withdraw': {
        'task': 'wallets.tasks.withdraw',
        "schedule": timedelta(seconds=5),
    },
}

app.conf.timezone = 'UTC'
