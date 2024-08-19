from django.urls import path
from django.contrib.auth import views as auth_views
from .views import XizmatlarView, loging, register, logoutview, servises, abouts, MessageView

urlpatterns = [
    path('xizmatlar/', XizmatlarView.as_view(), name='index'),
    path('login/', loging, name='loging'),
    path('register/', register, name='register'),
    path('logout/', logoutview, name='logout'),
    path('servises/', servises, name='servises'),
    path('about/', abouts, name='about'),
    path('messages/', MessageView.as_view(), name='messages'),
]