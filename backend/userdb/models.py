# Create your models here.
from django.db import models


class Password(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
