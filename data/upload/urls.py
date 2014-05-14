from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'public.views.home', name='home'),
    url(r'^queue/$', 'public.views.queue', name='queue'),

    url(r'^upload/$', 'public.views.upload', name='upload'),
    url(r'^migrate/$', 'public.views.migrate', name='migrate'),

    url(r'^manage/(?P<transaction>.*)/$', 'public.views.manage', name='manage'),

    url(r'^admin/', include(admin.site.urls)),
)
