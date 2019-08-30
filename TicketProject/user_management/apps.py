from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission


def create_group(name, permissions):
    group = Group.objects.create(name=name)
    [group.permissions.add(permission) for permission in permissions]


def define_ticket_groups(sender, **kwargs):
    admin_permissions = [
        Permission.objects.get(codename='add_user'),
        Permission.objects.get(codename='change_user'),
        Permission.objects.get(codename='view_user'),
        Permission.objects.get(codename='delete_user'),
        Permission.objects.get(codename='add_ticket'),
        Permission.objects.get(codename='change_ticket'),
        Permission.objects.get(codename='view_ticket'),
        Permission.objects.get(codename='delete_ticket'),
    ]
    create_group('super_admin', admin_permissions)

    senior_system_admin_permissions = [
        Permission.objects.get(codename='add_ticket'),
        Permission.objects.get(codename='change_ticket'),
        Permission.objects.get(codename='view_ticket'),
        Permission.objects.get(codename='assign_to'),
        Permission.objects.get(codename='view_system_admin'),
    ]
    create_group('senior_system_admin', senior_system_admin_permissions)

    system_admin_permissions = [
        Permission.objects.get(codename='change_state'),
        Permission.objects.get(codename='view_ticket'),
    ]
    create_group('system_admin', system_admin_permissions)


class UserManagementConfig(AppConfig):
    name = 'user_management'

    def ready(self):
        post_migrate.connect(define_ticket_groups, sender=self)
