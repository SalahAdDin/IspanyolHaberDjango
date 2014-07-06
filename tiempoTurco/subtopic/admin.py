from django.contrib import admin

from .models import Subtopic
from actions import export_as_excel
# Register your models here.

class SubtopicAdmin(admin.ModelAdmin):
    actions = (export_as_excel,)
    list_display = ('id','name', )
    list_editable = ('name',)
    list_filter = ('topic__name',)
    search_fields = ('topic__name', 'name',)

admin.site.register(Subtopic, SubtopicAdmin)