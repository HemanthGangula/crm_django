from django.urls import path, include
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
]