from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.views.generic import DetailView
from .views import NewsDefaultView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiempoTurco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    #Lo ideal es que cada mòdulo tenga su propio archivo de direcciones url las cuàles solo afecten el mòdulo

    url(r'^(?P<slug>[\w\-]+)/', 'news.views.New_view', name='New.view'),
    #url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[\w\-]+)/', NewsDefaultView.as_view(), name='NewsView'),

)