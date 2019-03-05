from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import register 


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]