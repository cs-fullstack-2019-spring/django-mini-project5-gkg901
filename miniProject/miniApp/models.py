from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class userModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16, default='')
    email = models.EmailField(default='')
    picture = models.CharField(max_length=1000, default='')
    userKey = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name






class mealModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    directions = models.TextField(default='')
    created = models.DateField(default=timezone.now)
    creator = models.ForeignKey(userModel, on_delete=models.SET_NULL, null=True, blank=True)
    pictureURL = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
