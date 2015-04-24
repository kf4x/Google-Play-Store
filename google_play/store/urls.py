from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from .views import IndexView, DetailView, ResultsView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'apps/details*$', DetailView.as_view(), name='app'),
    url(r'apps/details/(?P<slug>[\w-]+)$', DetailView.as_view(), name='app'),
    url(r'search/*$', ResultsView.as_view(), name='search'),
    
)
