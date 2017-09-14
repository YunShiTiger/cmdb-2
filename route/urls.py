# coding:utf-8
from django.conf.urls import patterns, include, url
from route.views import get_sidebar


urlpatterns = [
    url(r'^get_sidebar/$', get_sidebar, name='get_sidebar'),
]