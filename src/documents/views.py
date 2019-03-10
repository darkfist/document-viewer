from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from document_viewer.settings import CDN_DOMAIN

from .models import Document, DocumentUpload
from .forms import AddDocument


@login_required(login_url='/login/')
def add_documents(request):
	form = AddDocument(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():

			# looping through all image fields and saving it's name in a single string
			all_doc_url = str(form.cleaned_data.get('document'))
			for i in range(2,11):
				extra = 'document' + str(i)
				if (str(form.cleaned_data.get(extra)) != 'None'):
					all_doc_url = all_doc_url + " " + str(form.cleaned_data.get(extra))
			
			# saving the details in the db
			obj = Document.objects.create(
					title = form.cleaned_data.get('title'), 
					description = form.cleaned_data.get('description'),
					doc_url = all_doc_url,
					uploaded_by = request.user
				)
			
			# uploading the first image with same id
			query = Document.objects.latest('id')
			obj = DocumentUpload.objects.create(
					document_id = query.id,
					name = form.cleaned_data.get('title'),
					document_url = form.cleaned_data.get('document'),
				)
			
			# looping through all other images and uploading with same id
			for i in range(2,11):
				extra = 'document' + str(i)
				if (str(form.cleaned_data.get(extra)) != 'None'):
					obj = DocumentUpload.objects.create(
						document_id = query.id,
						name = form.cleaned_data.get('title'), 
						document_url = form.cleaned_data.get(extra),
					)
			return HttpResponseRedirect('/')
			
	if form.errors:
		errors = form.errors

	template_name = 'documents/add_documents.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)

def display_documents(request):
	template_name = 'documents/display_documents.html'

	# querying Image table from db
	queryset1 = Document.objects.all().order_by('-pk')

	# querying ImageUpload table from db
	queryset2 = DocumentUpload.objects.all()

	# domain of CDN where the documents will be uploaded
	cdn = CDN_DOMAIN
	
	context = {"object_list": queryset1, "document_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)

def user_documents(request):
	template_name = 'documents/user_documents.html'

	# querying Image table from db
	queryset1 = Document.objects.filter(uploaded_by=request.user).order_by('-pk')

	# querying ImageUpload table from db
	queryset2 = DocumentUpload.objects.all()

	# domain of CDN where the documents will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "document_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)