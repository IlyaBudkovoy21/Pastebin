from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя', help_text='Не более 15 символов')
    surname = models.CharField(max_length=15, verbose_name='Фамилия', help_text='Не более 15 символов')
    email = models.EmailField(null=True, blank=True)
    id_link = models.ForeignKey('Link', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return 'Пользователь'


class Link(models.Model):
    link = models.URLField(null=True, blank=True)
    active_link = models.DateField(null=True, blank=True)
