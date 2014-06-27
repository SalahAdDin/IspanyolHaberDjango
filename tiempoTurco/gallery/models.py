from django.db import models

from author.models import Author
from news.models import News

# Create your models here.
class Gallery (models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    news = models.OneToOneField(News) #No necesariamente