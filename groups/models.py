from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)

class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)