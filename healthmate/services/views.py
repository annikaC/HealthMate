"""Views for services."""

from django.views.generic import DetailView, TemplateView, CreateView
from django.utils.translation import ugettext as _

from categories_i18n.models import Category
from djgeojson.views import GeoJSONLayerView

from .models import Service
from .forms import ServiceForm


class ServiceJSONLayer(GeoJSONLayerView):
    def get_queryset(self):
        current_category = Category.objects.get(pk=self.kwargs.get('id', None))
        context = Service.objects.all().filter(categories=current_category)
        return context


class ServiceProfileView(DetailView):

    """A view for service profiles."""

    context_object_name = "service"
    model = Service
    template_name = "services/profile.html"


class ServicesView(TemplateView):

    """A view for services around your location."""
    template_name = "services/map.html"
    settings_overrides = {
        'MIN_ZOOM': 3,
        'MAX_ZOOM': 18,
        'RESET_VIEW': False,
    }

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        category_title = Category.objects.get(pk=self.kwargs.get('id'))
        context['title'] = _(category_title.title)
        return context


class ServiceFormView(CreateView):
    template_name = 'services/create_form.html'
    form_class = ServiceForm
    success_url = '/'
