from django.urls import path, include
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('customer/<int:pk>/', views.customer_records, name='customer_records'),
    path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
] 