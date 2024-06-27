from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django import forms
from .models import User


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm password')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), initial=None, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), initial=None, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')


class UserChangeDetailsForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False, initial=None)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, initial=None)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, initial=None)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False,
                               initial=None)


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control'}),
    )


class SetNewPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
