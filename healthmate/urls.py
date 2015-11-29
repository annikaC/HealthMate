"""URLs for website."""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from djgeojson.views import GeoJSONLayerView

from services.models import Service
from services.views import ServicesView, ServiceFormView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ServicesView.as_view(), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Service,
                                                    properties=('name', 'categories', 'additional_info',),
                                                    geometry_field="location"), name='data'),
    url(r'^services?/',
        include('healthmate.services.urls', namespace='services')),
    url(r'^markdown/', include('django_markdown.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,  # pragma: no cover
                          document_root=settings.MEDIA_ROOT)  # pragma:no cover
