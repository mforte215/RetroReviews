from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import generic
from .models import Article, VideoLink, Comment
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .forms import CustomUserCreationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging


logger = logging.getLogger("mylogger")

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

def movieFeed(request):
    latest_movie_list = Article.objects.filter(tags__name__in=["Movies"]).order_by('-pub_date')[:10]
    return render(request, 'application/movie-feed.html', {'latest_movie_list': latest_movie_list})

def gameFeed(request):
    latest_game_list = Article.objects.filter(tags__name__in=["Games"]).order_by('-pub_date')[:10]
    return render(request, 'application/game-feed.html', {'latest_game_list': latest_game_list})

def gadgetFeed(request):
    latest_gadget_list = Article.objects.filter(tags__name__in=["Gadgets"]).order_by('-pub_date')[:10]
    return render(request, 'application/gadget-feed.html', {'latest_gadget_list': latest_gadget_list})

def newDetailView(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    page = request.GET.get('page', 1)
    comments = article.comments.filter(active=True)
    comment = None
    username = None
    parent_id = None
    if request.user.is_authenticated:
        username = request.user.username;
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_id = comment_form['parent_id'].value()
            logger.info("-------------------------------")
            logger.info("Logging parent id:")
            logger.info(parent_id)
            logger.info("-------------------------------")
            if parent_id is not None and parent_id != '':
                parent = Comment.objects.get(pk=parent_id)
                comment = comment_form.save(commit=False)
                comment.parent = parent;
                comment.article = article
                comment.created_by = request.user
                comment.save()
                return redirect('articles:detail', article_id=article.id)
            else:
                comment = comment_form.save(commit=False)
                comment.article = article
                comment.created_by = request.user
                comment.save()
                return redirect('articles:detail', article_id=article.id)
    else:
        comment_form = CommentForm()
    return render(request, 'application/detail.html', {'article': article, 'comments': comments, 'comment': comment, 'comment_form': comment_form, 'username': username})




def videoDetail(request, video_id):
    videoLink = get_object_or_404(VideoLink, pk=video_id)
    return render(request, 'application/video-detail.html', {'videoLink': videoLink})

def videoFeed(request):
    latest_video_list = VideoLink.objects.order_by('-pub_date')[:10]
    return render(request, 'application/video-feed.html', {'latest_video_list': latest_video_list})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('articles:index'), RequestContext(request))
    registered = False
    if request.method == 'POST':
        user_form = CustomUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request, 'registration/registration_complete.html')

    else:
        user_form = CustomUserCreationForm()
    return render(request,'registration/register.html',
                          {'form':user_form})
