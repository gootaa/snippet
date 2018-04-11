from django.shortcuts import render, redirect
from django.http import HttpResponse #To be removed later
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import RegistrationForm, ProfileForm, EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def home(request):
	"""
	Placeholder view
	"""
	return HttpResponse('Hello, this is the home page')

def register(request):
	"""
	Handles RegistrationForm, login the new user,
	creates profile for the new user, and redirects 
	to home page
	"""
	if request.user.is_authenticated():
		return redirect('home')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)

			profile = Profile()
			profile.user = user
			profile.save()

			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'register.html', {'form':form})


@login_required
def profile_settings(request):
	"""
	Handles ProfileForm and responds to user
	using messages
	"""
	profile = request.user.profile
	if request.method == 'POST':
		form = ProfileForm(data=request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your profile was updated successfully!')
			return redirect('profile_settings')
		else:
			messages.warning(request, 'Please enter valid data.')
	else:
		form = ProfileForm(instance=profile)
	return render(request, 'profile-settings.html', {'form':form})


@login_required
def account_settings(request):
	"""
	Displays EmailForm and PasswordChangeForm
	"""
	email_form = EmailForm(instance=request.user)
	password_form = PasswordChangeForm(request.user)

	return render(request,
				'account-settings.html',
				{'email_form':email_form,
					'password_form':password_form})


@login_required
def change_email(request):
	"""
	Handles EmailForm and responds to user using messages
	"""
	if request.method == 'POST':
		form = EmailForm(instance=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Email was updated successfully!')
		else:
			messages.warning(request, 'Please enter valid data.')
	return redirect('account_settings')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please enter valid data')
    return redirect('account_settings')

