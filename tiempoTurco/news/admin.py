from django.contrib import admin

from .models import New
from actions import export_as_excel
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'topic', 'subtopic','dateTime')
    list_filter = ('author', 'title', 'topic', 'subtopic','dateTime')
    search_fields = ('author__first_name','author__last_name', 'title', 'topic', 'subtopic','dateTime') #si quiero buscar noticias por el apellido de su author 'author__last_name'
    list_editable = ('title', 'topic', 'subtopic')
    actions = (export_as_excel,)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(New, NewAdmin)
