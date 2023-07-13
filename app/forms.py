from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email','phone','address', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address','phone']


class ForgotPasswordForm(PasswordChangeForm):
    pass
