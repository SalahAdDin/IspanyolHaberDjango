from django.db import models

from news.models import New
# Create your models here.

class Comment(models.Model):
    news = models.ForeignKey(New)
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.name,self.dateTime)