from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    category=models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.URLField()
    rate=models.FloatField()
    count=models.IntegerField()
