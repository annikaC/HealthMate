"""URLs for services."""

from django.conf.urls import url

from .views import ServiceFormView


urlpatterns = [
    url(r'^new/$', ServiceFormView.as_view(), name='create_service'),
]
