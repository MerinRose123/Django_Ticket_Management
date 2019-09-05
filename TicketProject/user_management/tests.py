from django.test import TestCase

from .tasks import add
add.apply_async((4, 4), retry=False)