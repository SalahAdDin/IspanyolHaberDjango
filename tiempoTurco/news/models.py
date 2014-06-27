from django.db import models


from author.models import Author
from subtopic.models import Subtopic
from topic.models import Topic

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic)
    subtopic = models.ForeignKey(Subtopic)
    author = models.ForeignKey(Author)
    #linkAuthor = models.URLField() Como traerlo desde el propio autor?
    dateTime = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/news')
    content = models.TextField()
    source = models.URLField()
    slug =  models.SlugField()