from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

from blog.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/register/$', register, name='register'),
    url(r'', include('blog.urls')),
]
