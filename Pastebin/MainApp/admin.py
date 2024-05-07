from django.contrib import admin
from .models import User, Link


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'email')
    list_filter = ('surname', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
