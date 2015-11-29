"""URLs for services."""

from django.conf.urls import include, url

from .views import ServiceFormView, ServicesView


urlpatterns = [
    url(r'^map/$', ServicesView.as_view(), name='service_map'),
    url(r'^new/$', ServiceFormView.as_view(), name='create_service'),
]
