from django.db import models
from django.template.defaultfilters import slugify

from authors.models import Author
from subtopic.models import Subtopic
from topic.models import Topic
from keyWords.models import KeyWord

# Create your models here.

class New(models.Model):
    title = models.CharField(verbose_name='Título', max_length=255, unique=True)
    topic = models.ForeignKey(Topic, verbose_name='Tema')
    subtopic = models.ForeignKey(Subtopic, verbose_name='Subtema')
    author = models.ForeignKey(Author, verbose_name='Autor')
    #el enlace del autor se pasa en la vista de la noticia como new.author.link_own
    #image = models.como poner la imagen?
    keyword = models.ManyToManyField(KeyWord, blank=True, verbose_name='Palabras Clave')
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')
    place = models.CharField(max_length=255, verbose_name='Lugar')
    content = models.TextField(verbose_name='Contenido')
    source = models.URLField(verbose_name='Fuente', blank=True)
    slug =  models.SlugField(verbose_name='Slug', max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self):  #Definir metodo para guardar, validar y otros metodos del Slug
        super(New, self).save() #Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(New, self).save()

    def get_absolute_url(self):
        return '/news/%s/' % self.slug

    class Meta:
        ordering=['-dateTime']
        verbose_name_plural='Noticias'
    