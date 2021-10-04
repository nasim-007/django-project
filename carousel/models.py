from django.db import models

# Create your models here.


class Carousel(models.Model):

    title = models.CharField(max_length=40)
    image = models.ImageField()

    def __str__(self):
        return self.title
    