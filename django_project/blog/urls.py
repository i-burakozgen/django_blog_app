from django.contrib import admin
from django.urls import path
from . import views
#when user goes to blog route after rest of it blog urls gonna handle
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
    
]
