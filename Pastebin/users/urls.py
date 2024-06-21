from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.personal_account, name='default'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_reset/', views.reset_password, name='reset_password'),
    path('password_reset/password_reset_done/', views.password_reset_done, name='password_reset_done'),
]
