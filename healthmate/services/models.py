"""Contains the Service and ServiceImage models."""

from django.contrib.gis.db import models as geo_models
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField
from django_markdown.models import MarkdownField
from categories_i18n.models import Category


class Service(geo_models.Model):

    """The service model."""

    categories = models.ManyToManyField(Category)
    slug = AutoSlugField(
        populate_from='name', max_length=30, unique=True, editable=False,
        always_update=True)
    name = models.CharField(
        _("Service Name"), max_length=100,
        help_text=_("This name will be used to identify your service."))
    additional_info = MarkdownField(blank=True)
    # Geo Django field to store a point
    location = geo_models.PointField(
        help_text=_("Represented as (longitude, latitude)"),
        default="POINT(0.0 0.0)")

    # You MUST use GeoManager to make Geo Queries
    objects = geo_models.GeoManager()

    def __unicode__(self):
        """Return name representation for service."""
        return self.name

    def get_absolute_url(self):
        """Get profile url for link in admin."""
        return reverse('services:profile', kwargs={
            'slug': self.slug
        })

    @property
    def popupContent(self):
      return '<p>{}</p>'.format(
          self.name)


class ServiceImage(models.Model):

    """Images on the service profile."""

    service = models.ForeignKey(Service, related_name='images')
    image = models.ImageField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
