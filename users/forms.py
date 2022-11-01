
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone_no=forms.CharField(max_length=13)
    firs_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)

    class Meta:
        model=User
        fields=['username','email','phone_no', 'password1','password2']