from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = patterns('website',
    (r'^$', TemplateView.as_view(template_name = 'index.html') ),
    (r'^about/$', TemplateView.as_view(template_name ='about/index.html') ),
    (r'^contact/$', TemplateView.as_view(template_name ='contact/index.html') ),
    (r'^contribute/$', TemplateView.as_view(template_name ='contribute/index.html') ),
    (r'^developers/$', TemplateView.as_view(template_name ='developers/index.html') ),
    (r'^government/$', TemplateView.as_view(template_name ='government/index.html') ),
)