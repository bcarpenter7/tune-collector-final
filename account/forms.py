from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import MyUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', help_text='')
    password = forms.CharField(label='Password', help_text='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username', 'autofocus': True})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter Password'})


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput, max_length=254, help_text='Required')
    email = forms.EmailField(label='Email', widget=forms.EmailInput, max_length=254, help_text='Required')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html
    )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, help_text='Re-enter Password')

    class Meta:
        model = MyUser
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username', 'autofocus': True})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'placeholder': 'email@address.com'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Create Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Reenter Password'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if MyUser.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
