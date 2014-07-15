from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','name','caption','ImageNotice','news')
    list_filter = ('name','id',)
    list_editable = ('name','caption')
    search_fields = ('name','news__title','news__author')
    def ImageNotice(self, obj):
            return '<img src="%s" alt="%s" title="%s">' % (get_thumbnail(obj.image, '100x100').url, obj.name, obj.name)
    ImageNotice.allow_tags = True

admin.site.register(Image, ImageAdmin)