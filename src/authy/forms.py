from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterPageForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}), max_length=16)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}), max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}), max_length=35)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}), max_length=35)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), max_length=35)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), max_length=35)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class LoginPageForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}), max_length=16)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    error_messages = {
        'invalid_login': 'Usuario y/o contrasena incorrectos',
    }
