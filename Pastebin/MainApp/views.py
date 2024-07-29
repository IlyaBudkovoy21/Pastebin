from django.shortcuts import render
from .forms import TextForm
from .s3 import client
import asyncio


# Create your views here.
def save_text(request):
    with open('file1', 'w') as f:
        f.writelines(request.POST['paste'])
    asyncio.run(client.upload_file('file1'))


def home(request):
    if request.method == 'POST':
        save_text(request)
    text_description = 'Веб-приложение, которое позволяет загружать отрывки текста, обычно фрагменты исходного кода, для возможности просмотра окружающими. Такой сервис очень популярен среди пользователей IRC-сетей, где вставка больших фрагментов текста на каналы считается плохим тоном. Сервис также часто используется пользователями IM. В интернете существует множество pastebin веб-приложений, большинство из которых предоставляет подсветку синтаксиса различных языков программирования и специальной разметки.'
    text_welcome = 'Добро пожаловать на сайт Pastebin!'
    context = {
        'text_description': text_description,
        'text_welcome': text_welcome,
        'user': request.user,
        'form': TextForm()
    }
    return render(request, 'MainApp/MainPage.html', context=context)
