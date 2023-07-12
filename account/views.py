from django.shortcuts import render, redirect
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
			return redirect('/')
	else:
		form = RegistrationForm()
		
	context = {
		'form': form
	}
	return render(request, 'account/registration/register.html', context)

