# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from .models import AndroidApplication, hamming_stats
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader



class IndexView(generic.TemplateView):
    template_name = 'store/index.djhtml'

    
class DetailView(generic.View):
    model = AndroidApplication
    template_name = 'store/detail.djhtml'

    def get(self, request, *args, **kwargs):
        try:
            pkg  = self.kwargs["package"]
            self.object= AndroidApplication.objects.get(package=pkg)
            self.object.description = self.object.description
            self.object.percentrating = (self.object.rating/5.0)*100
            
        except Exception, e:
            print e

        t = loader.get_template('store/detail.djhtml')
        c = RequestContext(request, self.object)
        return render_to_response(
            'store/detail.djhtml',
            {'object':self.object},
            context_instance=RequestContext(request)
        )
                          


class ResultsView(generic.ListView):
    template_name = 'store/results.djhtml'
    
    def get_queryset(self):
        cont = self.request.GET.get('q')
        return AndroidApplication.objects.filter(name__contains=cont)[:20]
    
    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        # add data to context about this result
        stats = hamming_stats(context['object_list'])
        context['hamming'] = stats
        return context
