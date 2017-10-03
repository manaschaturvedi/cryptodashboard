from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect


def homepage(request):
	if request.user.is_authenticated():
		current_user = request.user
		return redirect('/dashboard/'+str(current_user.id))
	return render(request, 'homepage.html')