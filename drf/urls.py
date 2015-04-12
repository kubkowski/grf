from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # Examples:
    # url(r'^$', 'drf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
