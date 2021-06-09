from .models import URL

from loguru import logger


@logger.catch
def add_object_to_db_if_not_exitst(long_url, short_url, max_clicks):
    """Add an object to the database if the similar object does not exist"""
    if not URL.objects.filter(short_url=short_url).exists():
        URL(long_url=long_url, short_url=short_url,
            max_clicks=max_clicks).save()
        logger.debug('new object has been created')


@logger.catch
def click(url):
    """Add +1 (click) to count_clicks"""
    url.count_clicks += 1
    logger.debug('add +1 click to count_clicks')
    url.save()
    logger.debug('save object')


@logger.catch
def max_clicks_check(url):
    """Check is count_clicks = max_clicks if True, delete URL object"""
    if not url.count_clicks == 0:
        if url.count_clicks >= url.max_clicks:
            url.delete()
            logger.debug('delete object, because clicks limit expired')
