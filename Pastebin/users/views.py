from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request, 'users/PersonalAccount/PersonalAccount.html', {'user': form})
    form = UserLoginForm()
    return render(request, 'users/registration/login.html', {'form': form})


def registration(request):

    return render(request, 'users/registration/registration.html')


def registration_success(request):
    return render(request, 'users/registration/registration_success.html')


def personal_account(request):
    try:
        if request.user.is_authenticated() is not None:
            username = request.user.get_username()
            return render('users/PersonalAccount/PersonalAccountIn.html',
                          context={'username': username})
    except:
        return render(request, 'users/PersonalAccount/PersonalAccount.html')


def logout(request):
    return render(request, 'users/registration/logout.html')
