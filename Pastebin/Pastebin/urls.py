from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls as file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls', namespace='main_page'), name='Home'),
    path('accounts/', include('users.urls', namespace='users'), name='accounts'),
]
