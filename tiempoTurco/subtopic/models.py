from django.db import models

# Create your models here.
from tiempoTurco.topic.models import Topic


class Subtopic(models.Model):
    name = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic)
