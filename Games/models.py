from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    creator = models.CharField(max_length=225)
    genre = models.CharField(max_length=225)
    year = models.ImageField()