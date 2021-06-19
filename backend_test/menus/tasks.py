from datetime import datetime

from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from backend_test.celery import app
from backend_test.menus.models import Menu
from backend_test.menus.utils import slack_notifier

logger = get_task_logger(__name__)


@app.task()
def send_menu(template: str, destiny: str):
    """
    Task to send the menu to destiny, the notifier
    is a callable, with the special logic for each destiny

    """
    logger.info("Executing task")
    return slack_notifier(template, destiny)


@periodic_task(run_every=(crontab(hour=11)))
def close_menu():

    try:
        menu = Menu.objects.get(date=datetime.now().date())
        menu.closed = True
        menu.save()
        closed = menu.closed
    except Menu.DoesNotExist:
        closed = False
    return closed
