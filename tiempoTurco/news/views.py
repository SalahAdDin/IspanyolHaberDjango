import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404

from .models import New

# Create your views here.
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