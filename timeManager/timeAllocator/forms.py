from django.contrib.auth.forms import UserCreationForm
from django import forms

from timeAllocator.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta(forms.ModelForm):
        model = User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta(forms.ModelForm):
        model = User
