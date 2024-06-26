from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:aasan>/video_feed/', views.video_feed, name='video_feed'),
    path('<str:aasan>/', views.index, name='aasan'),
]