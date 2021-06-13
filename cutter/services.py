from .models import URL


def add_object_to_db_if_not_exitst(long_url, short_url):
    """Add an object to the database if the similar object does not exist"""
    if not URL.objects.filter(short_url=short_url).exists():
        URL(long_url=long_url, short_url=short_url).save()
