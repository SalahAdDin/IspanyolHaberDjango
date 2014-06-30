from django.db import models

from gallery.models import Gallery
from news.models import New

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/news')
    caption = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery)
    news = models.ForeignKey(New)

    def __str__(self):
        return self.name
