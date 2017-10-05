"""app URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import serializers, viewsets, routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views

from rest_framework.routers import DefaultRouter

from snippets.views import UserCreateView
from snippets.views import UserView
from snippets.views import GroupCreateView
from snippets.views import GroupView
from snippets.views import SnippetCreateView # Import views from snippet app
from snippets.views import SnippetView
from snippets.views import FileCreateView
from snippets.views import FileView

# DRF includes utilities for creating/modifying user accounts (Including Forgot Password methods)
#router = routers.DefaultRouter()
#router.register(r'users', UserView, 'list')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # For the default Django Rest Framework admin interface
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'), # For token authorization! Allows AJAX client to POST username and password and receive a token
    url(r'^users/$', UserCreateView.as_view(), name="view"),
    url(r'^user/(?P<pk>[0-9]+)$', UserView.as_view(), name="view"),
    url(r'^groups/$', GroupCreateView.as_view(), name="create"),
    url(r'^group/(?P<pk>[0-9]+)$', GroupView.as_view(), name="view"),
    url(r'^snippets/$', SnippetCreateView.as_view(), name="create"),
    url(r'^snippet/(?P<pk>[0-9]+)$', SnippetView.as_view(), name="view"), # pk is the variable used to get the object
    url(r'^files/$', FileCreateView.as_view(), name="create"),
    url(r'^file/(?P<pk>[0-9]+)$', FileView.as_view(), name="create")
	# jobs/1/
    #url(r'^v1/', include('api.urls')), #Include routes created in API app -> to domain.com/v1/ - or api.quicksnipp.com/v1/
]
