from django.contrib.auth.models import Group
from django.test import TestCase

from django.test import TestCase
class GroupTestCase(TestCase):
    def test_group_creation(self):
        group = Group.objects.create(name="Math Study")
        self.assertEqual(group.name, "Math Study")