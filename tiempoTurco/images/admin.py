from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','name','caption','ImageNotice',)
    list_filter = ('name','id',)
    list_editable = ('name','caption')
    search_fields = ('name',)
    def ImageNotice(self, obj):
            return '<img src="%s">' % get_thumbnail(obj.image, '100x100').url
    ImageNotice.allow_tags = True

admin.site.register(Image, ImageAdmin)