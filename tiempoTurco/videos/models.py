from django.db import models

from gallery.models import Gallery
from news.models import New

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery)
    news = models.OneToOneField(New)

    def __str__(self):
        return self.name