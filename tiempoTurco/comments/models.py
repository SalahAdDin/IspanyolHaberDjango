from django.db import models

from news.models import New
# Create your models here.

class Comment(models.Model):
    news = models.ForeignKey(New, verbose_name='Noticia')
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='Nombre', max_length=50)
    content = models.TextField(verbose_name='Contenido')
    dateTime = models.DateTimeField(verbose_name='Fecha y Hora', auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.name,self.dateTime)

    class Meta:
        ordering=['-dateTime']
        verbose_name_plural='Comentarios'