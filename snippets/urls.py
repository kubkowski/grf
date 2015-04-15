from django.cong.urls import url
from snippets import view

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^/snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]