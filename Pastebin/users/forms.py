from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "Username", 'placeholder': "Username", 'type': 'text',
               'id': 'UserName'}
    ))
    password = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "Password", 'placeholder': "Password", 'type': 'text',
               'id': 'PasswordUser'}
    ))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "first_name", 'placeholder': "first_name",
               'type': 'text',
               'id': 'FirstNameUser'}))
    last_name = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "last_name", 'placeholder': "last_name",
               'type': 'text',
               'id': 'LastNameUser'}))
    username = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "username", 'placeholder': "username",
               'type': 'text',
               'id': 'UserName'}))
    email = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "email", 'placeholder': "Email", 'type': 'text',
               'id': 'EmailUser'}
    ))
    password1 = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "password", 'placeholder': "Password", 'type': 'text',
               'id': 'PasswordUser'}
    ))
    password2 = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', "name": "password", 'placeholder': "Password", 'type': 'text',
               'id': 'PasswordUser'}
    ))

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
