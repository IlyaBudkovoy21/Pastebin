from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal_account, name='default'),
    path('registration/', views.registration, name='registration'),
    path('registration_success/', views.registration_success),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
