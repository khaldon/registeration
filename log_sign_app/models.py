from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SignUp(models.Model):
    username = models.CharField(blank=False, max_length=100)
    email = models.EmailField()
    password = models.CharField(blank=False, max_length=100)
    re_password = models.CharField(blank=False, max_length=100, default='')
    def __str__(self):
        return self.username

class LogIn(models.Model):
    username = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
