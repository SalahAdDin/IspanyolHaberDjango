from django.db import models

from gallery.models import Gallery
from news.models import New

# Create your models here.
class Image(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255)
    image = models.ImageField(verbose_name='Imagen', upload_to='images/news')
    caption = models.CharField(verbose_name='Descripción', max_length=255)
    gallery = models.ForeignKey(Gallery, verbose_name='Galería')
    news = models.ForeignKey(New, verbose_name='Noticias')

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-name']
        verbose_name_plural='Imágenes'
