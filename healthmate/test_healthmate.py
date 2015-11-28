#!/usr/bin/env python

from django.test import TestCase


class MainTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response['Content-Type'])

    def test_page_not_found(self):
        response = self.client.get("/notherelol")
        self.assertEqual(response.status_code, 404)


class ServicesPageTest(TestCase):

    def test_services(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)
