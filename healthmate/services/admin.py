"""Admin functionality for services."""
from django.contrib import admin
from django.contrib.admin import site

from leaflet.admin import LeafletGeoAdmin

from .models import Category, Service, ServiceImage


class ServiceImageInline(admin.TabularInline):

    """The inline for service images."""

    model = ServiceImage
    extra = 3
    ordering = ("order",)


class ServiceAdmin(LeafletGeoAdmin, admin.ModelAdmin):

    """The class for the service admin."""

    inlines = [ServiceImageInline]


site.register(Service, ServiceAdmin)
site.register(Category)
