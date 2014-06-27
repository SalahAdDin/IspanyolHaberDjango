from django.db import models

from news.models import News
# Create your models here.

class Comments(models.Model):
    news = models.ForeignKey(News)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

