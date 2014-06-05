from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = patterns('website',
    (r'^$', TemplateView.as_view(template_name='website/index.html') ),
    (r'^about/$', TemplateView.as_view(template_name='website/about/index.html') ),
    (r'^contact/$', TemplateView.as_view(template_name='website/contact/index.html') ),
    (r'^contribute/$', TemplateView.as_view(template_name='website/contribute/index.html') ),
    (r'^developers/$', TemplateView.as_view(template_name='website/developers/index.html') ),
    (r'^government/$', TemplateView.as_view(template_name='website/government/index.html') ),
)
