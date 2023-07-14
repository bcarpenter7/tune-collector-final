from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegistrationForm


def user_registration_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.email = form.cleaned_data['email']
			user.set_password(form.cleaned_data['password2'])
			user.save()
			messages.add_message(request, messages.SUCCESS, 'Account created, please log in')
			return redirect(reverse_lazy('account:login'))
	else:
		form = RegistrationForm()
		
	context = {
		'form': form
	}
	return render(request, 'account/registration/register.html', context)


def user_deletion_view(request):
	if not request.user.is_authenticated:
		return redirect('/')
	return render(request, 'account/delete.html')
	

def user_deletion_confirm(request):
	if request.user.is_authenticated:
		request.user.is_active = False
		request.user.save()
		messages.add_message(request, messages.SUCCESS, 'Account deleted')
		return redirect('/')
