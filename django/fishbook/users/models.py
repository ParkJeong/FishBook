from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50)
    userPw = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User({self.email}, {self.userPw}, {self.created_at}, {self.updated_at})'
# Create your models here.
