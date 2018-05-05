from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^urlinfo/1/(?P<host>(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9][0-9]|[0-9]?)(\.(25[0-5]|2[0-4][0-9]|[1][0-9][0-9]|[1-9][0-9]|[0-9]?)){3})/(?P<port>[0-9]{4})/(?P<original_path>[A-Za-z0-9\/]+)', views.ResourceDetails.as_view({"get": "retrieve"}))
]


urlpatterns = format_suffix_patterns(urlpatterns)
