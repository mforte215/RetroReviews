from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import Article


class IndexView(generic.ListView):
    template_name = 'application/index.html'
    context_object_name = 'latest_article_list'
    
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Article
    template_name = 'application/detail.html'