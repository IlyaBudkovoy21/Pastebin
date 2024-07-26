from django.shortcuts import render
import boto3


# Create your views here.
def home(request):
    text_description = 'Веб-приложение, которое позволяет загружать отрывки текста, обычно фрагменты исходного кода, для возможности просмотра окружающими. Такой сервис очень популярен среди пользователей IRC-сетей, где вставка больших фрагментов текста на каналы считается плохим тоном. Сервис также часто используется пользователями IM. В интернете существует множество pastebin веб-приложений, большинство из которых предоставляет подсветку синтаксиса различных языков программирования и специальной разметки.'
    text_welcome = 'Добро пожаловать на сайт Pastebin!'
    context = {
        'text_description': text_description,
        'text_welcome': text_welcome,
        'user': request.user,
    }
    return render(request, 'MainApp/MainPage.html', context=context)


def send_text(request):
    # Create a resource service client by name using the default session.
    s3 = boto3.resource('s3')
