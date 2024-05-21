from django.shortcuts import render, redirect
from .forms import UserData
from django.http import HttpRequest


# Create your views here.
def home(request):
    text_description = 'Веб-приложение, которое позволяет загружать отрывки текста, обычно фрагменты исходного кода, для возможности просмотра окружающими. Такой сервис очень популярен среди пользователей IRC-сетей, где вставка больших фрагментов текста на каналы считается плохим тоном. Сервис также часто используется пользователями IM. В интернете существует множество pastebin веб-приложений, большинство из которых предоставляет подсветку синтаксиса различных языков программирования и специальной разметки.'
    text_welcome = 'Добро пожаловать на сайт Pastebin!'
    context = {
        'text_description': text_description,
        'text_welcome': text_welcome
    }
    return render(request, 'MainApp/MainPage.html', context=context)


