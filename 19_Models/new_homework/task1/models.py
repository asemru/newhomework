from django.db import models
# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=31)
    password = models.TextField()
    age = models.IntegerField()


class Games(models.Model):
    title = models.TextField()
    cost = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.TextField()






