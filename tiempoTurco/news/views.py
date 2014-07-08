import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import New

# Create your views here.

class NewsDefaultView(DetailView):
    template_name = 'news_template.html'
    queryset = New.objects.all()
    context_object_name = 'news'
    slug_field = 'slug'

    #def get_queryset(self):


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class NewsIndexView(ListView):
    template_name = 'index.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by',  self.paginate_by)

    def get_queryset(self):
        return New.objects.filter()

def New_view(request, slug):
    new = get_object_or_404(New, slug=slug)

    data = {
        'title': new.title,
        'topic': new.topic.name,
        'subtopic': new.subtopic.name,
        #'datetime': new.dateTime,
        'place': new.place,
        'content': new.content,
        #'keyworsds': new.keyword.name,
        'source': new.source,
        #se puede anidar mas datos, por ejemplo
        'author':{
            'first_name': new.author.first_name,
            'last_name': new.author.last_name,
            'link_own': new.author.link_own,
        }
    }

    json_data = json.dumps(data)
    #json.loads(string_json) Cargar una cadena json

    return HttpResponse(json_data, content_type='application/json')
    #return render(request, 'author.html', {'author': author})