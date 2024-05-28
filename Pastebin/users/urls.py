from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.personal_account, name='default'),
    path('registration/', views.registration, name='registration'),
    path('registration/registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),

]
