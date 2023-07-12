from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserLoginForm(AuthenticationForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
