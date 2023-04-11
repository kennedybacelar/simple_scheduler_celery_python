from tasks import app
from celery.schedules import crontab

app.conf.beat_schedule = {
    "export-job": {
        "task": "tasks.schedule_activities",
        "schedule": crontab(minute="*"),
    },
}