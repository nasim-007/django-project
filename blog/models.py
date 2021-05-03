from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)