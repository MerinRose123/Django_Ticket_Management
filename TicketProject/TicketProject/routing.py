from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from user_management.consumers import NotConsumer

# Routing asynchronous communication to conswmer NotConsumer.
application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotConsumer),
    ])
})