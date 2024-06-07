from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import User


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = User.objects.get(email=email.lower()).username
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password, backend='users.authenticate.EmailBackend')
            if user is not None:
                login(request, user, backend='users.authenticate.EmailBackend')
                return redirect('users:personal_account')
            else:
                messages.error(request, 'This user has not been found')
                return redirect('users:login')
        else:
            messages.error(request, 'Incorrect email or password')
            return redirect('users:login')
    else:
        form = UserLoginForm()
        return render(request, 'users/registration/login.html', {'form': form})


def registration_success(request):
    return render(request, 'users/registration/registration_success.html')


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = User.objects.get(email=email.lower()).username
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password, backend='users.authenticate.EmailBackend')
            login(request, user, backend='users.authenticate.EmailBackend')
            messages.success(request, 'Registration successful')
            return redirect(reverse('users:personal_account'))
        else:
            return render(request, 'users/registration/registration.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'users/registration/registration.html', {'form': form})

def personal_account(request):
    if request.user.is_authenticated:
        return render(request, 'users/PersonalAccount/PersonalAccountIn.html')
    else:
        return render(request, 'users/PersonalAccount/PersonalAccount.html')


def logout_user(request):
    logout(request)
    return render(request, 'users/registration/logout.html')
