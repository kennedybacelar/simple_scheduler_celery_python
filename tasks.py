from datetime import datetime
from typing import List
from celery import Celery
from structlog import get_logger
from time import sleep
from database_mock import database

FILENAME = "z_log_activities.txt"

logger = get_logger(__name__)
app = Celery('tasks', broker="redis://localhost:6385/0", backend="redis://localhost:6385/0")


def pretty_format_date(datetime_object: datetime):
    return datetime.strftime(datetime_object, "%H:%M:%S")

@app.task
def log_activity(database_obj):
    
    logger.info(" *** Logging actiity *** ")
    
    days_of_job_execution: List[int] = database_obj["export_schedule_week_days"]
    if datetime.today().weekday() in days_of_job_execution:
        with open(FILENAME, "a+") as f:
            string_to_be_inserted = f"{database_obj['id']}-{database_obj['workspace_name']} *** {pretty_format_date(datetime.now())}"
            f.write(f"{string_to_be_inserted}\n")

@app.task
def schedule_activities():
    logger.info(" *** Executing schedule activities *** ")
    for database_obj in database:
        log_activity.delay(database_obj)
    