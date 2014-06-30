from django.contrib import admin

from .models import Author
from actions import export_as_excel
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('news_own', 'first_name', 'last_name', 'age','link_own')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name','news_own') #si quiero buscar noticias por el apellido de su author 'author__last_name'
    list_editable = ('first_name', 'last_name', 'age','link_own')
    actions = (export_as_excel,)

admin.site.register(Author, AuthorAdmin)
