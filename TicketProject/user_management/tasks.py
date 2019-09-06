from celery import Celery
from django.shortcuts import render, redirect
from celery.utils.log import get_task_logger
from datetime import date

app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@localhost:6379//')
logger = get_task_logger(__name__)


@app.task(ignore_result=True)
def add(x, y):
    print("Function works")
    return x + y


@app.task(name="send")
def send(tickets):
    """sends data to view function when current date is greater than end date in ticket"""
    logger.info("Sent")
    for ticket in tickets:
        if date.today() > ticket.end_date:
            print("Function works")
    return redirect('../home/')