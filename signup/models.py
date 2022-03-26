import email
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.EmailField(default="NULL@email.com")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)