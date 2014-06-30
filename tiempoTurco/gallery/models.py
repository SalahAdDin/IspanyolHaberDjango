from django.db import models

from authors.models import Author
from news.models import New

# Create your models here.
class Gallery (models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    news = models.OneToOneField(New) #No necesariamente

    def __str__(self):
        return self.name