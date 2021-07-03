from cutter.models import URL
from cutter.services import add_object_to_db_if_not_exitst, url_to_one_kind

from django.test import TestCase


class ServicesTestCase(TestCase):
    def setUp(self):
        URL(long_url='test.com', short_url='99ab715d84').save()

    def test_add_object_to_db_if_not_exitst(self):
        assert URL.objects.filter(short_url='test.com').exists() == False
        assert URL.objects.filter(short_url='99ab715d84').exists() == True
        add_object_to_db_if_not_exitst('99ab715d84', 'test.com')
        assert URL.objects.filter(short_url='test.com').exists() == True

    def test_url_to_one_kind(self):
        assert url_to_one_kind('test.com') == 'test.com'
        assert url_to_one_kind('https://test.com') == 'test.com'
        assert url_to_one_kind('http://test.com') == 'test.com'
        assert url_to_one_kind('https://www.test.com') == 'test.com'
        assert url_to_one_kind('http://www.test.com') == 'test.com'
        assert url_to_one_kind('www.test.com') == 'test.com'
