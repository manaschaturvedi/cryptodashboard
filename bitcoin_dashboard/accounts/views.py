from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import login,logout,get_user_model,authenticate


def user_signup(request):
	form = UserSignupForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request,new_user)
		current_user = request.user
		return redirect('/dashboard/'+str(current_user.id))
	return render(request, 'signup.html', {'form':form})


def user_login(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		current_user = request.user
		return redirect('/dashboard/'+str(current_user.id))
	return render(request, 'login.html', {'form':form})


def user_logout(request):
	logout(request)
	return redirect('/')
