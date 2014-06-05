from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('website.urls')),

    url(r'^upload/', include('upload.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('sfapp.urls')),
)
