from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField('users.User', related_name='joined_groups', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_create(user):
        return user.is_superuser or user.role == 'professor'


class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='group_files/', blank=True, null=True)
    image = models.ImageField(upload_to='group_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_post(user):
        return user.role == 'professor'
