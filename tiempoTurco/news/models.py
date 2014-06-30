from django.db import models
from django.template.defaultfilters import slugify

from authors.models import Author
from subtopic.models import Subtopic
from topic.models import Topic

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic)
    subtopic = models.ForeignKey(Subtopic)
    author = models.ForeignKey(Author)
    #el enlace del autor se pasa en la vista de la noticia como new.author.link_own
    #image = models.como poner la imagen?
    dateTime = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=255)
    content = models.TextField()
    source = models.URLField(blank=True)
    slug =  models.SlugField()

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(New, self).save()