from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=24)
    adress = models.CharField(max_length=50, default='')
    age = models.IntegerField(null=True)
    description = models.CharField(max_length=255, default='', blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name