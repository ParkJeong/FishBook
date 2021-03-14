from django.db import models


class Admin(models.Model):
    adminId = models.CharField(max_length=20)
    adminPw = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    bookmark = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
