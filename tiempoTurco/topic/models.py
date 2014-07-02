from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Temas'


