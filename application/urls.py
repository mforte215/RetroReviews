from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.newIndexView, name='index'),
    path('article/<int:article_id>/', views.newDetailView, name='detail'),
    path('movies/', views.movieFeed, name='moviefeed'),
    path('games/', views.gameFeed, name='gamefeed'),
    path('gadgets/', views.gadgetFeed, name='gadgetfeed'),
    path('videos/', views.videoFeed, name='videofeed'),
    path('video/<int:video_id>/', views.videoDetail, name='detailvideo'),
]
