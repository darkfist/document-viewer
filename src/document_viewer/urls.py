from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^', include('documents.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.WEB_URL, document_root=settings.WEB_ROOT)
    urlpatterns += static(settings.BUILD_URL, document_root=settings.BUILD_ROOT)
