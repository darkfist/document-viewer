from django.conf.urls import url

from .views import display_documents, add_documents, document_details, user_documents


urlpatterns = [
    url(r'^view-documents/$', display_documents, name='view'),
    url(r'^my-documents/$', user_documents, name='user_doc'),
    url(r'^document-details/(?P<slug>[\w-]+)/$', document_details, name='details'),
    url(r'^add/$', add_documents, name='add'),
]