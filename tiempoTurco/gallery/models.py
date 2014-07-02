from django.db import models

from authors.models import Author
from news.models import New

# Create your models here.
class Gallery (models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255)
    caption = models.CharField(verbose_name='Descripción', max_length=255)
    author = models.ForeignKey(Author, verbose_name='Autor')
    news = models.OneToOneField(New, verbose_name='Noticia', blank=True) #No necesariamente, problema, no se como ponerlo opcional

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-name']
        verbose_name_plural='Galería'