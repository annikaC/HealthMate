#!/usr/bin/env python

from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from model_mommy import mommy
from .models import Service


class ServiceTest(TestCase):
    def setUp(self):  # NOQA
        self.service = mommy.make(Service,
                                    name="Test Service",
                                    slug="test-service",
                                    make_m2m=True)

    def test_profile_page(self):
        response = self.client.get(reverse('services:profile', args=(
            self.generator.slug)))
        self.assertEqual(response.status_code, 200)

    def test_absolute_url(self):
        response = self.client.get(self.service.get_absolute_url())
        self.assertEqual(response.status_code, 200)
