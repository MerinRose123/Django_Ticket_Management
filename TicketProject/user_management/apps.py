from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    """
    To run signals
    """
    name = 'user_management'

    def ready(self):
        from . import signals
