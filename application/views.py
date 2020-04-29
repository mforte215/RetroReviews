from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from .models import Article, VideoLink
from django.views import View
from django.http import HttpResponse




class IndexView(generic.ListView):
    template_name = 'application/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'application/detail.html'


def newIndexView(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    latest_top_article = Article.objects.filter(tags__name__in=["Top Stories"]).order_by('-pub_date')[0]
    second_latest_top_article = Article.objects.filter(tags__name__in=["Top Stories"]).order_by('-pub_date')[1]
    third_latest_top_article = Article.objects.filter(tags__name__in=["Top Stories"]).order_by('-pub_date')[2]
    fourth_latest_top_article = Article.objects.filter(tags__name__in=["Top Stories"]).order_by('-pub_date')[3]
    latest_video_list = VideoLink.objects.order_by('-pub_date')[:5]
    return render(request, 'application/index.html', {'latest_article_list': latest_article_list, 'latest_top_article': latest_top_article, 'second_latest_top_article': second_latest_top_article, 'third_latest_top_article': third_latest_top_article, 'fourth_latest_top_article': fourth_latest_top_article, \
    'latest_video_list': latest_video_list })

def newDetailView(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'application/detail.html', {'article': article})
