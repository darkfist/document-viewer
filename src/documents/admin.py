from django.contrib import admin


from .models import Document, DocumentUpload

admin.site.register(Document)
admin.site.register(DocumentUpload)