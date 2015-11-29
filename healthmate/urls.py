"""URLs for website."""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from categories_i18n.views import CategoryListView

from services.models import Service
from services.views import ServicesView, ServiceJSONLayer


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^data.geojson/(?P<id>\d+)$', ServiceJSONLayer.as_view(model=Service,
                                                    properties=('name', 'categories', 'additional_info', 'popupContent',),
                                                    geometry_field="location"), name='data'),
    url(r'^services?/',
        include('healthmate.services.urls', namespace='services')),
    url(r'^category/search/$', CategoryListView.as_view(), name='categories_list'),
    url(r'^category/(?P<id>\d+)/map/$', ServicesView.as_view(), name='category_detail'),
    url(r'^markdown/', include('django_markdown.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,  # pragma: no cover
                          document_root=settings.MEDIA_ROOT)  # pragma:no cover
