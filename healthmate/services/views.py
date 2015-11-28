"""Views for services."""

from django.views.generic import DetailView, RedirectView

from .models import Service


class ServiceProfileView(DetailView):

    """A view for service profiles."""

    context_object_name = "service"
    model = Service
    template_name = "services/profile.html"

