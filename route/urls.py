# coding:utf-8
from django.conf.urls import patterns, include, url
from route.views import get_sidebar,get_routing_info


urlpatterns = [
    url(r'^get_sidebar/$', get_sidebar, name='get_sidebar'),
    url(r'^get_routing_info/$', get_routing_info, name='get_routing_info'),

]