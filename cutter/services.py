from .models import URL


def add_object_to_db_if_not_exitst(long_url, short_url):
    """Add an object to the database if the object does not exist"""
    if not URL.objects.filter(short_url=short_url).exists():
        URL(long_url=long_url, short_url=short_url).save()


def url_to_one_kind(initial_url):
    """Cut initial_url to one kind without http/https and www"""
    if initial_url[0:7] == 'http://':
        initial_url = initial_url[7:]
    if initial_url[0:8] == 'https://':
        initial_url = initial_url[8:]
    if initial_url[0:4] == 'www.':
        initial_url = initial_url[4:]
    return initial_url
