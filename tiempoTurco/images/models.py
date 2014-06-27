from django.db import models

from gallery.models import Gallery
from news.models import News

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery)
    news = models.ForeignKey(News)
