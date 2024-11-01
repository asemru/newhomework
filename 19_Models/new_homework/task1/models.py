from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.TextField()
    balance = models.TextField(models.DecimalField)
    age = models.TextField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.TextField()
    cost = models.TextField(models.DecimalField)
    size = models.TextField(models.DecimalField)
    description = models.TextField()
    age_limited = models.BooleanField(False)
    buyer = models.ManyToManyField(Buyer, related_name='courses')
    DecimalField = models.IntegerField()
    BooleanField = models.BooleanField()

    def __str__(self):
        return self.title
