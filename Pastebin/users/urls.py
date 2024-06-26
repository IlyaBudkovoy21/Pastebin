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
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
]
