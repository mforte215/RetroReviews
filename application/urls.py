from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.newIndexView, name='index'),
    path('<int:article_id>/', views.newDetailView, name='detail'),
]
