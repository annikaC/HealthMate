"""Views for services."""

from django.http import JsonResponse
from django.views.generic import DetailView, TemplateView, CreateView

from .models import Service
from .forms import ServiceForm


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


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


class ServiceFormView(CreateView):
    template_name = 'services/create_form.html'
    form_class = ServiceForm
    success_url = '/'
