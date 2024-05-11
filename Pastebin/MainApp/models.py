from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя', help_text='Не более 15 символов')
    surname = models.CharField(max_length=15, verbose_name='Фамилия', help_text='Не более 15 символов')
    email = models.EmailField(null=True, blank=True)
