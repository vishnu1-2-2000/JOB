from django import forms
from.models import Signup_User
# from django.contrib.auth.models import User

from django.contrib.auth.forms import  UserCreationForm
# authentication/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)