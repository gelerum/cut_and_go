from cutter.models import URL

from django.test import TestCase


class ViewsTestCase(TestCase):
    def setUp(self):
        URL(long_url='test.com', short_url='99ab715d84').save()

    def test_index_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_redirect_view(self):
        response = self.client.get('/99ab715d84/')
        self.assertEqual(response.status_code, 302)
