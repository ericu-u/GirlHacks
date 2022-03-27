import email
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.EmailField(default="NULL@email.com")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    excercise = models.IntegerField()
    diet = models.CharField(max_length=100)
    