"""URLs for services."""

from django.conf import settings
from django.conf.urls import include, url

from . import views

service_urls = [
    url(r"^$", views.ServiceProfileView.as_view(), name="profile"),
]

urlpatterns = [
    url(r"^(?P<slug>[^/]+)/", include(service_urls)),
]
