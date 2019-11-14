from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Client
from django.db.models import Q

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Client
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Client.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )