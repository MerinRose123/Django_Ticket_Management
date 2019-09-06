from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery
from TicketProject.settings.local import BROKER_URL
from datetime import datetime

celery = Celery('tasks', broker=BROKER_URL)


@shared_task(name="change_state")
def change_state(date1):
    """
    To run the worker type the command below in the terminal.
    celery -A user_management.tasks worker --loglevel=info

    :param date1:The end_date fetched from model Ticket
    :return: True if the current date is greater than end date.
            False if end date is greater than today.
    """
    end_date = datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S')
    today = datetime.now()
    if today > end_date:
        print('The end date is less than today.')
        return True
    else:
        print("The end date is greater than today.")
        return False

