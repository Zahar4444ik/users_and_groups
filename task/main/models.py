from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Permission, Group


class CustomGroup(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, blank=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    user_group = models.ForeignKey(CustomGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
