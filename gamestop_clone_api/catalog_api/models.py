from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    image = models.CharField(max_length=255)