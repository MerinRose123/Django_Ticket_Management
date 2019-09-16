from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery
from TicketProject.settings.local import BROKER_URL
from datetime import datetime
from .models import Ticket

celery = Celery('tasks', broker=BROKER_URL)


@shared_task(name="change_state")
def change_state():
    """
    To run the worker type the command shown below in the terminal.
    celery -A user_management.tasks worker --loglevel=info

    :param date1:The end_date fetched from model Ticket
    :return: True if the current date is greater than end date.
            False if end date is greater than today.
    """
    tickets = Ticket.objects.all()
    for ticket in tickets:
        end_date = datetime.strptime(ticket.end_date, '%Y-%m-%dT%H:%M:%S')
        today = datetime.now()
        if today > end_date:
            print('The end date is less than today.')
            ticket.state = "CAN"
            ticket.save()
            return True
        else:
            print("The end date is greater than today.")
            return False

