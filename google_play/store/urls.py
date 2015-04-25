from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from .views import IndexView, DetailView, ResultsView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'apps/details/(?P<package>[^/]+)*$', DetailView.as_view(), name='app_details'),
    #url(r'apps/details/(?P<package>[\w])$', DetailView.as_view(), name='app'),
    url(r'search/*$', ResultsView.as_view(), name='search'),
    
)
