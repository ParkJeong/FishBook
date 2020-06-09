from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=20)
    userPw = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    rrn = models.CharField(max_length=200)
    last_destination = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
