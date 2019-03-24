from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


from .forms import UserRegisterForm


def register(request):
	form = UserRegisterForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		messages.success(request, 'Account created successfully! Now login to continue.')
		return HttpResponseRedirect('/users/login/')
	
	if form.errors:
		errors = form.errors

	template_name = 'users/register.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)