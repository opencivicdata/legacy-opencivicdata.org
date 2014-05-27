from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('home',
    url(r'^$', 'views.home', name='home'),
)
