from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(verbose_name='Nombres', max_length=255)
    last_name = models.CharField(verbose_name='Apellidos', max_length=255, blank=True)
    biography = models.TextField(verbose_name='Biografía', blank=True)
    age = models.PositiveIntegerField(verbose_name='Edad')
    link_own = models.URLField(verbose_name='Enlace Propio', blank=True)
    news_own = models.PositiveIntegerField(verbose_name='Noticias', blank=True, default='0') #Contador de publicaciones que ha tenido, entre Articulos, COlumnas, Galerias, pueden ser propias o referidas

    class Meta:
        ordering=['-last_name']
        verbose_name_plural='Autores'

    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('authors.views.Author_view', None, {'first_name': self.first_name})