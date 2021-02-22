import datetime
import django.contrib.auth.models
import django.utils
from django.db import models

from django.utils import timezone

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=24, primary_key=True)
    hierarchy = models.IntegerField(default=0)

    def __str__(self):
         return self.name

class User(models.Model):
    name = models.CharField(max_length=24)
    adress = models.CharField(max_length=50, default='')
    age = models.IntegerField(null=True)
    description = models.CharField(max_length=255, default='', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default='',blank=True)

    def __str__(self):
         return self.name

    def was_created_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=7)