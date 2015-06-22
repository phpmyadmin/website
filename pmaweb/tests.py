from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTest(TestCase):
    fixtures = ['test_data.json']

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'phpMyAdmin')
        response = self.client.get('/')
        self.assertContains(response, 'phpMyAdmin')

    def test_themes(self):
        response = self.client.get(reverse('themes'))
        self.assertContains(response, 'Metro')
