from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),

    url(r'^upload/', include('upload.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),

    url(r'^logout/$', 'sunlightauth.views.logout', name='logout'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('sfapp.urls')),
)
