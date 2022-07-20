from django.db import models


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    mail = models.EmailField()
    password = models.CharField(max_length=255)
    company = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    is_admin = models.BooleanField()
