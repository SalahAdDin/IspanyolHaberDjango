from django.contrib import admin

from .models import Topic
from subtopic.models import Subtopic
from actions import export_as_excel

# Register your models here.
class SubtopicInLine(admin.StackedInline):
    model = Subtopic

class TopicAdmin(admin.ModelAdmin):
    actions = (export_as_excel,)
    inlines = [SubtopicInLine, ]
    list_display = ('id', 'name', )
    list_editable = ('name',)
    search_fields = ('name',)

admin.site.register(Topic, TopicAdmin)