# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from .models import AndroidApplication, hamming_stats
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.db.models import Q


__author__="Javier C"

class IndexView(generic.TemplateView):
    template_name = 'store/index.djhtml'


class AppDetailView(generic.View):
    """Used to display details of a Application."""

    def get(self, request, *args, **kwargs):

        pkg  = self.kwargs["package"]
        # get the record from the store
        self.object = AndroidApplication.objects.get(package=pkg)

        dev = self.object.developer
        if dev:
            more = AndroidApplication.objects.filter(
                developer=dev).exclude(pk=self.object.pk)[:5]
        else:
            more = []

        return render_to_response(
            'store/detail.djhtml',
            {'object': self.object,
             'more': more},
            context_instance=RequestContext(request)
        )

class DevDetailView(generic.ListView):
    """View for getting apps by developer"""
    
    template_name = 'store/results.djhtml'
    
    def get_queryset(self):
        dev = self.kwargs['dev']
        return AndroidApplication.objects.filter(developer=dev)

    def get_context_data(self, **kwargs):
        # Set the page title
        kwargs['page'] = 'More by '+ self.kwargs['dev']
        return append_hamming(DevDetailView, self, **kwargs)

class SearchResultsView(generic.ListView):
    """View for searching the store"""
    
    template_name = 'store/results.djhtml'

    def get_queryset(self):
        # Get the keyword passed in through url params
        cont = self.request.GET.get('q')

        # Search if name or description contains keyword
        # return AndroidApplication.objects.filter(
        #     Q(name__contains=cont) | Q(description__contains=conte))[:40]
        
        # search if name contains keyword
        return AndroidApplication.objects.filter(name__contains=cont)[:40]

    def get_context_data(self, **kwargs):
        # set the page title
        kwargs['page'] = 'Apps'
        return append_hamming(SearchResultsView, self, **kwargs)


# util
def append_hamming(cls, inst, **kwargs):
    """Adds hamming stats to the context

    Args:
        cls - the class that is iheriting from super
        inst - the instance most likly self 
        kwargs - just the args for context
    Returns:
       context - the context will have hamming and page which can be 
    referenced in the view"""

    
    context = super(cls, inst).get_context_data(**kwargs)
    # add data to context about this result
    stats = hamming_stats(context['object_list'])
    context['hamming'] = stats
    context['page'] = kwargs.get('page', '')
    return context
