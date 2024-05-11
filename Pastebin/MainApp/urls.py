from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('registration/', views.registration, name='registration'),
    path('registration/registration_success/', views.registration_success),
    path('personal_account/', views.PersonalAccount),
]
