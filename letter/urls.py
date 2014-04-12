from django.conf.urls import patterns, include, url

from . import views

letter_pk = r'(?P<letter_pk>\d+)'
filter_choice = r'(?P<filter_choice>\d+)'
order_choice = r'(?P<order_choice>\d+)'

urlpatterns = patterns('esport',
    url(r'^letter/$', views.letter_index, name='letter_index'),
    url(r'^letter/list_view/$', views.letter_list_view, name='letter_list'),
    url(r'^letter/single_view/{}/$'.format(letter_pk), views.letter_single_view, name='single_letter_view'),
    url(r'^letter/query_view/{}/{}/$'.format(filter_choice, order_choice), views.letter_query_view, name='letter_query_view'),
 )