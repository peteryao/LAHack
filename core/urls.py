from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core.views',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),

)