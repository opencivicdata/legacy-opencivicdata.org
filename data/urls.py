from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('website.urls')),

    url(r'^upload/', include('upload.urls')),
    url(r'^admin/edit/', include(admin.site.urls)),
    url(r'^admin/$', 'reports.views.report', name='report'),

    url('', include('social.apps.django_app.urls', namespace='social')),
)
