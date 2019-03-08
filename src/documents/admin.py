from django.contrib import admin

# Register your models here.
from .models import Document, DocumentUpload

admin.site.register(Document)
admin.site.register(DocumentUpload)