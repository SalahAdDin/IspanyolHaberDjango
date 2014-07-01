from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiempoTurco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # Grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #Lo ideal es que cada mòdulo tenga su propio archivo de direcciones url las cuàles solo afecten el mòdulo
    #Here own urls for module
    url(r'^authors/', include('authors.urls')), #Authors Urls
    url(r'^gallery/', include('gallery.urls')), #Gallery Urls
    url(r'^keyWords/', include('keyWords.urls')), #keyWords Urls
    url(r'^news/', include('news.urls')), #News Urls
    url(r'^subtopic/', include('subtopic.urls')), #Subtopic Urls
    url(r'^topic/', include('topic.urls')), #Topic Urls
    url(r'^users/', include('userProfiles.urls')),  #Users Urls


    #url(r'^authors/(?P<first_name>[\w\-]+)/', 'authors.views.Author_view', name='Author.view'),
    #url(r'^registerUser/', 'userProfiles.views.signUp',name='signUp'),
    #url(r'^loginUser/', 'userProfiles.views.loginUser',name='logIn'),
)

if settings.DEBUG: #Django server maneja media solo cuando esta en desarrollo, ideal que en produccion otro server los maneje, no entiendo esto
    urlpatterns += patterns(
        '',
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }
        ),
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )