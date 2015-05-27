from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from .views import IndexView, AppDetailView, SearchResultsView, DevDetailView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'apps/details/(?P<package>[^/]+)*$', AppDetailView.as_view(), name='app_details'),
    url(r'apps/developer/(?P<dev>[^/]+)*$', DevDetailView.as_view(), name='more_by_dev'),
    #url(r'apps/details/(?P<package>[\w])$', DetailView.as_view(), name='app'),
    url(r'search/*$', SearchResultsView.as_view(), name='search'),
    
)
