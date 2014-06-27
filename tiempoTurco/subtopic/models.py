from django.db import models

from topic.models import Topic

# Create your models here.

class Subtopic(models.Model):
    name = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic)
