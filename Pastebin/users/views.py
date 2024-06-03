from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('users:personal_account'))
    form = UserLoginForm()
    return render(request, "users/registration/login.html", {'form': form})


def registration_success(request):
    return render(request, 'users/registration/registration_success.html')


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect(reverse('users:registration_success'))
        else:
            return render(request, 'users/registration/registration.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'users/registration/registration.html', {'form': form})


def personal_account(request):
    if request.user.is_authenticated:
        return render(request, 'users/PersonalAccount/PersonalAccountIn.html')
    return render(request, 'users/PersonalAccount/PersonalAccount.html', {'user': request.user})


def logout_user(request):
    logout(request)
    return render(request, 'users/registration/logout.html')


def update_user(request):
    if request.method == 'POST':
        form =
