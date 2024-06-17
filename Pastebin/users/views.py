from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm, UserChangeDetailsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password, backend='users.authenticate.EmailBackend')
        if user is not None:
            login(request, user, backend='users.authenticate.EmailBackend')
            return redirect('users:personal_account')
        else:
            messages.error(request, 'This user has not been found')
            return redirect('users:login')
    else:
        form = UserLoginForm()
        return render(request, 'users/registration/login.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password, backend='users.authenticate.EmailBackend')
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


def edit_profile(request):
    if request.method == "POST":
        form = UserChangeDetailsForm(request.POST)
        print(form)
        if form.is_valid():
            user = User.objects.get(email=request.user.email)
            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['email'] is not None:
                if user.is_verified:
                    user.email = form.cleaned_data['email']
                else:
                    messages.add_message(request, messages.ERROR,
                                         'It is not possible to update the email because your last email is not verified')
            user.save()
            return redirect('users:personal_account')
        else:
            print('не валидна')
            return render(request, 'users/PersonalAccount/editProfile.html', context={'form': form})
    else:
        form = UserChangeDetailsForm()
        context = {'form': form}
        return render(request, 'users/PersonalAccount/editProfile.html', context=context)
