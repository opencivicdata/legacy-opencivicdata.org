from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('data.upload',
    url(r'^$', 'views.home', name='home'),
    url(r'^queue/$', 'views.queue', name='queue'),

    url(r'^upload/$', 'views.upload', name='upload'),
    url(r'^migrate/$', 'views.migrate', name='migrate'),

    url(r'^manage/(?P<transaction>.*)/$', 'views.manage', name='manage'),
)
