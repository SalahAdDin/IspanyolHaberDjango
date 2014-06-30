from django.db import models

from news.models import New

# Create your models here.
class KeyWord(models.Model):
    name = models.CharField(max_length=50)
    news = models.ManyToManyField(New)

    def __str__(self):
        return self.name