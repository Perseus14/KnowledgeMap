from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Client, Project
from django.db.models import Q

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Project
    template_name = 'search_results.html'

    def or_parser(self, query):
        flag = False
        values = None
        if '+' in query or '|' in query:
            flag = True
            values = list(map(str.lstrip, map(str.rstrip, query.split('+'))))
            if len(values) == 1:
                values = list(map(str.lstrip, map(str.rstrip, query.split('|'))))
        return flag, values

    def and_parser(self, query):
        flag = False
        values = None
        if '&' in query:
            flag = True
            values = list(map(str.lstrip, map(str.rstrip, query.split('&'))))
        return flag, values

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        query = query.lstrip().rstrip()
        flag, values = self.or_parser(query)
        res = []
        if flag:
            res += [Project.objects.filter(
                Q(tags__name__iexact=query) | Q(client__name__icontains=query)
            ) for query in values]
        else:
            flag, values = self.and_parser(query)
            if flag:
                res += [Project.objects.filter(
                    Q(tags__name__iexact=query) | Q(client__name__icontains=query)
                ) for query in values]
            else:
                res += [Project.objects.filter(
                    Q(tags__name__iexact=query) | Q(client__name__icontains=query)
                )]

        final_res = []
        for res_ele in res:
            final_res += res_ele

        final_res = set(final_res)
        print(final_res)
        for obj in final_res:
            print(obj.client)
        return final_res
