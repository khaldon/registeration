from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(blank=False, max_length=100)
    email = models.EmailField()
    password = models.CharField(blank=False, max_length=100)
    re_password = models.CharField(blank=False, max_length=100)

class LogIn(models.Model):
    username = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
