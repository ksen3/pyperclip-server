from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username',
        'aria-label': 'Username',
        'aria-describedby': 'username_field'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password',
        'aria-label': 'Password',
        'aria-describedby': 'password_field'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Repeat password',
        'aria-label': 'Repeat password',
        'aria-describedby': 'repeat_password_field'
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username',
        'aria-label': 'Username',
        'aria-describedby': 'username_field'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password',
        'aria-label': 'Password',
        'aria-describedby': 'password_field'
    }))

