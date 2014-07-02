from django.db import models

from topic.models import Topic

# Create your models here.

class Subtopic(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255)
    topic = models.ForeignKey(Topic, verbose_name='Tema')

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-name']
        verbose_name_plural='Subtemas'
