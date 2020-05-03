from django.urls import path, include
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
    path('register/', views.register, name='signup'),
    path('comment/<int:comment_id>/', views.commentDetailView, name='commentdetail' )

]
