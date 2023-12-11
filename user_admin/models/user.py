from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.CharField(max_length=100, verbose_name='Email')
    active = models.BooleanField(default=True)
