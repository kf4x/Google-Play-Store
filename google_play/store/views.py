from django.shortcuts import render
from django.views import generic
from .models import AndroidApplication

class IndexView(generic.TemplateView):
    template_name = 'store/index.djhtml'

    
class DetailView(generic.DetailView):
    model = AndroidApplication
    template_name = 'store/detail.djhtml'

    def get(self, request, *args, **kwargs):

        self.object = {'app':'name'}
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)

    
class ResultsView(generic.ListView):

    template_name = 'store/results.djhtml'

    def get_queryset(self):
        """All apps"""
        return AndroidApplication.objects.all()
