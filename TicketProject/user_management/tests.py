from django.test import TestCase

from .tasks import add
# To test the celery app
add.apply_async((4, 4), retry=False)