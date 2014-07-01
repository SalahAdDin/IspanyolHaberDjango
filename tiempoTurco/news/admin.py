from django.contrib import admin

from .models import New
from actions import export_as_excel
from images.models import Image
from keyWords.models import KeyWord
# Register your models here.

class ImageInLine(admin.StackedInline):
    model = Image

class keyWordInLine(admin.StackedInline):
    model = KeyWord

class NewAdmin(admin.ModelAdmin):
    actions = (export_as_excel,)
    inlines = [ImageInLine, keyWordInLine, ]
    list_display = ('author', 'title', 'topic', 'subtopic','dateTime')
    list_filter = ('author', 'title', 'topic', 'subtopic','dateTime')
    list_editable = ('title', 'topic', 'subtopic')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('author__first_name','author__last_name', 'title', 'topic', 'subtopic','dateTime') #si quiero buscar noticias por el apellido de su author 'author__last_name'

admin.site.register(New, NewAdmin)
