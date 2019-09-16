from .models import *
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from.serializers import UserSerializer


@receiver(post_save, sender=User)
def announce_new_user(sender, instance, created, **kwargs):
    """
    Give a notification to everyone when a new user is added to the system
    """
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event": "New User",
                       "username": instance.username})


@receiver(post_delete, sender=User)
def post_delete_handler(sender, instance, **kwargs):
    """
    Called when row is deleted.
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {"type": "user.gossip",
                   "event": "Delete User",
                   "username": instance.username})


@receiver(post_save, sender=Ticket)
def announce_new_ticket(sender, instance, created, **kwargs):
    """
    Send a notification to the respective system admin when a new ticket is assigned to her.
    """
    if instance.assigned_to is not None:
        serializer = UserSerializer(data=instance.assigned_to)
        json = serializer.initial_data
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event": "New Ticket",
                       "ticket_id": instance.ticket_id,
                       "assigned_to": json.username,
                       })


@receiver(post_delete, sender=Ticket)
def announce_ticket_delete(sender, instance, **kwargs):
    """
    called when an existing ticket is deleted.
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {"type": "user.gossip",
                   "event": "Ticket Deleted",
                   "ticket_id": instance.ticket_id,
                   "assigned_to": instance.state,
                   })


@receiver(post_save, sender=Ticket)
def announce_ticket_done(sender, instance, created, **kwargs):
    """
    Giving notification to senior_system_admin when a ticket is moved to done state.
    """
    if instance.state == "DNE":
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event": "Ticket Done",
                       "ticket_id": instance.ticket_id,
                       "assigned_to": instance.state,
                       })
