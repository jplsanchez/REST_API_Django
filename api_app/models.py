from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=true)

    def __str__(self):
         return self.description