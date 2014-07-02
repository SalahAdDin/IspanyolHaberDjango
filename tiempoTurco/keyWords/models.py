from django.db import models

# Create your models here.
class KeyWord(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Palabras Clave'