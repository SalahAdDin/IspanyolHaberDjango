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

    #Reiniciar la contrasena en caso de perdida
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='admin_password_reset_done'),
    url(r'^admin/password_reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='admin_password_reset_confirm'),
    url(r'^admin/password_done/$', 'django.contrib.auth.views.password_reset_complete', name='admin_password_reset_complete'),

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

    #Pagina principal
    #url(r'^$', 'signups.views.home', name='home'),
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
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}
        ),
    )