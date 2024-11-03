from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True, verbose_name="Время появления статьи")

    def __str__(self):
        return self.title