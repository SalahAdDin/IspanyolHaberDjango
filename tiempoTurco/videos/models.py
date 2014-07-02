from django.db import models

from gallery.models import Gallery
from news.models import New

# Create your models here.
class Video(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255)
    caption = models.CharField(verbose_name='Descripción', max_length=255)
    gallery = models.ForeignKey(Gallery, verbose_name='Galería')
    news = models.OneToOneField(New, verbose_name='Noticia')
    video = models.URLField(verbose_name='Video')

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-name']
        verbose_name_plural='Videos'
