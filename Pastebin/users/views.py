from django.shortcuts import render, redirect, HttpResponse, reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.views import LoginView


# Create your views here.
class UserLogin(LoginView):
    template_name = 'users/registration/login.html'
    form_class = UserLoginForm
    success_url = 'users/PersonalAccount/PersonalAccountIn.html'

def registration_success(request):
    return render(request, 'users/registration/registration_success.html')


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect(reverse('users:registration_success'))
        else:
            return render(request, 'users/registration/registration.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'users/registration/registration.html', {'form': form})


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
