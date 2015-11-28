"""Views for services."""

from django.views.generic import DetailView, TemplateView

from .models import Service


class ServiceProfileView(DetailView):

    """A view for service profiles."""

    context_object_name = "service"
    model = Service
    template_name = "services/profile.html"


class ServicesView(TemplateView):

    """A view for services around your location."""
    template_name = "home.html"
    settings_overrides = {
        'MIN_ZOOM': 3,
        'MAX_ZOOM': 18,
        'RESET_VIEW': False,
    }
