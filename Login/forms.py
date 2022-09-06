from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class SignUpForm(UserCreationForm):
    """This is form that will be used for signup and Model is taken from Models.py"""
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class LogInForm(forms.Form):
    """Form that will be used for Login"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)