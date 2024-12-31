from django.db import models

# Create your models here.


class Rsvp(models.Model):
    name = models.CharField(max_length=100)
    attendance = models.BooleanField()
    message = models.TextField(max_length=200, null=True)
