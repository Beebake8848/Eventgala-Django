from django.db import models

# Create your models here.

class logins(models.Model):
    name = models.TextField(default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=128, default=None)