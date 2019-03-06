from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Document
from .forms import AddDocument


@login_required(login_url='/login/')
def add_documents(request):
	form = AddDocument(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			all_doc_url = str(form.cleaned_data.get('document'))
			for i in range(2,11):
				extra = 'document' + str(i)
				if (str(form.cleaned_data.get(extra)) != 'None'):
					all_doc_url = all_doc_url + " " + str(form.cleaned_data.get(extra))

			obj = Document.objects.create(
					title = form.cleaned_data.get('title'), 
					description = form.cleaned_data.get('description'),
					doc_url = all_doc_url,
					uploaded_by = request.user
				)

			return HttpResponseRedirect('/')
			
	if form.errors:
		errors = form.errors

	template_name = 'documents/add_documents.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)

def display_documents(request):
	template_name = 'documents/display_documents.html'
	queryset = Document.objects.all().order_by('-pk')
	context = {"object_list": queryset}
	return render(request, template_name, context)

def user_documents(request):
	template_name = 'documents/user_documents.html'
	queryset = Document.objects.filter(uploaded_by=request.user).order_by('-pk')
	context = {"object_list": queryset}
	return render(request, template_name, context)