from django.shortcuts import render, HttpResponse
from .forms import UserData


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserData(request.POST)
        if form.is_valid():
            return HttpResponse('<h1>Пасибо ебать!</h1>')
    text_description = 'Веб-приложение, которое позволяет загружать отрывки текста, обычно фрагменты исходного кода, для возможности просмотра окружающими. Такой сервис очень популярен среди пользователей IRC-сетей, где вставка больших фрагментов текста на каналы считается плохим тоном. Сервис также часто используется пользователями IM. В интернете существует множество pastebin веб-приложений, большинство из которых предоставляет подсветку синтаксиса различных языков программирования и специальной разметки.'
    text_welcome = 'Добро пожаловать на сайт Pastebin!'
    context = {
        'text_description': text_description,
        'text_welcome': text_welcome
    }
    return render(request, 'MainApp/MainPage.html', context=context)


def registration(request):
    form = UserData()
    return render(request, 'registration/registration.html', {'form': form})


def registration_success(request):
    if request.method == 'POST':
        user_data = UserData(request.POST)
        if user_data.is_valid():
            user_data.save()
        return render(request, 'registration/RegistrationSuccess.html')


def PersonalAccount(request):
    return render(request, 'PersonalAccount/PersonalAccount.html')
