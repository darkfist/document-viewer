"""image_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from documents.views import display_documents, add_documents, document_details
from users.views import register 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^documents/', include('documents.urls')),
    url(r'^/', include('users.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)