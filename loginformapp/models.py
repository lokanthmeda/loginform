from django.db import models


class register(models.Model):
    username = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=100)
