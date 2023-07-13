from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . models import Profile


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}), required=True)


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            (f"{value} already exist."), params={'value': value})


class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}), required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), required=True, validators=[validate_email])
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class ForgotPasswordForm(PasswordChangeForm):
    pass


# PROFILE
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'mobile', 'city',
                  'address', 'zipcode', 'province']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'form-control'}),
        }
