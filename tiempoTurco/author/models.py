from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    age = models.PositiveIntegerField()
    link_own = models.URLField()

