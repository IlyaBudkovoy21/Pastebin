from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class MyLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/registration/login.html'
    success_url = reverse_lazy('users:login')
    def dispath(self, request):
        if request.method == 'POST':
            form = self.get_form(request.POST)
            if form.is_valid():
                self.handle_login(form)
            else:
                print('хуйня форма')
        return super().dispatch(request)

    def handle_login(self, form):
        user = form.get_user()
        if user is not None:
            if user.is_active:
                return redirect(reverse('users:personal_account'))
            else:
                messages.error(self.request, 'Your account has not been confirmed by mail')
                return redirect(reverse('users:login'))
        else:
            messages.error(self.request, 'There is no such account. Try to register.')
            return redirect(reverse('users:login'))


def registration_success(request):
    return render(request, 'users/registration/registration_success.html')


class RegistrationView(FormView):
    template_name = "users/registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:registration_success')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        form.save()
        return super().form_valid(form)


def personal_account(request):
    if request.user.is_authenticated:
        return render(request, 'users/PersonalAccount/PersonalAccountIn.html')
    return render(request, 'users/PersonalAccount/PersonalAccount.html', {'user': request.user})


def logout_user(request):
    logout(request)
    return render(request, 'users/registration/logout.html')
