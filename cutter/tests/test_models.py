from cutter.models import URL

from django.test import TestCase


class URLTestCase(TestCase):
    def setUp(self):
        URL(long_url='test.com', short_url='99ab715d84').save()

    def test_get_object(self):
        url = URL.objects.get(long_url='test.com')
        self.assertEqual(url.short_url, '99ab715d84')
