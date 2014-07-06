from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiempoTurco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    #Lo ideal es que cada mòdulo tenga su propio archivo de direcciones url las cuàles solo afecten el mòdulo

    url(r'^(?P<slug>[\w\-]+)/', 'news.views.New_view', name='New.view'),
)