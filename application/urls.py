from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.newIndexView, name='index'),
    path('<int:article_id>/', views.newDetailView, name='detail'),
    path('video/<int:video_id>/', views.videoDetail, name='detailvideo'),
    path('movies/', views.movieFeed, name='moviefeed')
]
