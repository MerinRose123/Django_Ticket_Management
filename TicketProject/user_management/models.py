from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
from phone_field import PhoneField
import datetime


# Changing the base user fields
class User(AbstractUser):
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')

    class Meta:
        db_table = 'user'
        default_permissions = [('add_user', 'add new user'),
                               ('change_user', 'change existing user details'),
                               ('delete_user', 'delete a user'),
                               ('view_user', 'view current users')
                               ]
        permissions = [('view_system_admin', 'Can view system admins'),
                       ]

    def __str__(self):
        return self.username


# Adding the table ticket in database
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()
    subject = models.CharField(null=True, blank=True, max_length=100)
    message = models.CharField(null=True, blank=True, max_length=255)

    # choices for state
    CREATED = 'CRT'
    PROGRESS = 'PRG'
    DONE = 'DNE'
    STATE_CHOICES = [
        (CREATED, 'created'),
        (PROGRESS, 'in progress'),
        (DONE, 'done or cancelled'),
    ]
    state = models.CharField(
        max_length=3,
        choices=STATE_CHOICES,
        default='created'
    )

    # Choices for adding priority
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    PRIORITY_CHOICES = [
        (LOW, 'low priority'),
        (MEDIUM, 'medium priority'),
        (HIGH, 'high priority'),
    ]
    state = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='low'
    )

    class Meta:
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'
        db_table = 'ticket'
        ordering = ['ticket_id', 'assigned_to']
        permissions = [('change_state', 'Can change state'),
                       ('assign_to', 'can assign system admin')
                       ]
        default_permissions = [('add_ticket', 'add new ticket'),
                               ('change_ticket', 'change existing ticket'),
                               ('delete_ticket', 'delete a ticket'),
                               ('view_ticket', 'view the current ticket')
                               ]

    def __str__(self):
        return self.ticket_id

