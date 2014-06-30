import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Author

# Create your views here.
def Author_view(request, first_name):
    author = get_object_or_404(Author, first_name=first_name)

    data = {
        'f_name': author.first_name,
        'l_name': author.last_name,
        'bio': author.biography,
        'age': author.age,
        'l_own': author.link_own,
        #se puede anidar mas datos, por ejemplo
        #'author':{
            #'first_name': author.first_name
            #'last_name': author.last_name
            #'link_own': author.link_own
        # }
    }

    json_data = json.dumps(data)
    #json.loads(string_json) Cargar una cadena json

    return HttpResponse(json_data, content_type='application/json')
    #return render(request, 'author.html', {'author': author})