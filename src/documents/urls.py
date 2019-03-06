from django.conf.urls import url

from .views import display_documents, add_documents, user_documents


urlpatterns = [
    url(r'^$', display_documents, name='view'),
    url(r'^my-documents/$', user_documents, name='user_doc'),
    url(r'^add/$', add_documents, name='add'),
]