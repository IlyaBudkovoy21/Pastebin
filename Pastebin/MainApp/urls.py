from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main_page'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('accounts/', include('users.urls'), name='accounts'),

]
