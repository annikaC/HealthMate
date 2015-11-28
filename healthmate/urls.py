"""URLs for website."""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^services?/',
        include('healthmate.services.urls', namespace='services')),
    url(r'^markdown/', include('django_markdown.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,  # pragma: no cover
                          document_root=settings.MEDIA_ROOT)  # pragma:no cover
