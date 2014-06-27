from django.db import models

from news.models import News

# Create your models here.
class KeyWords(models.Model):
    name = models.CharField(max_length=50)
    news = models.ManyToManyField(News)