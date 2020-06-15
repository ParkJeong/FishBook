from django.db import models

# Create your models here.
class Post(models.Model):
    species = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.CharField(max_length = 200)
    view_count = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
