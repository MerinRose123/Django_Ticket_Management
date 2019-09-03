from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, label='first name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, label='first name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    phone = forms. CharField(max_length=50, label='phone',
                             widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
