from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    age = models.PositiveIntegerField()
    link_own = models.URLField(blank=True)
    news_own = models.PositiveIntegerField(blank=True,default='0') #Contador de publicaciones que ha tenido, entre Articulos, COlumnas, Galerias, pueden ser propias o referidas

    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)