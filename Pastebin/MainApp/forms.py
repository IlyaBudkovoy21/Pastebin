from django import forms
from .models import User


class UserData(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email']

    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField()
