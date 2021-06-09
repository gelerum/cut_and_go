from hashlib import sha256
from loguru import logger

from .models import URL
from .services import add_object_to_db_if_not_exitst, click, max_clicks_check
from django.shortcuts import render, redirect, get_object_or_404


@logger.catch
def add_new_url_view(request):
    """View for start page with form long_url"""
    if request.method == 'POST':
        temp = request.POST["long_url"]
        long_url = temp
        if temp[0:7] == 'http://':
            long_url = temp[7:]
            if long_url[0:4] == 'www.':
                long_url = long_url[4:]
        elif temp[0:8] == 'https://':
            long_url = temp[8:]
            if long_url[0:4] == 'www.':
                long_url = long_url[4:]
        elif temp[0:4] == 'www.':
            long_url = long_url[4:]
        max_clicks = request.POST["max_clicks"]
        short_url = sha256((long_url + str(max_clicks)).encode()) \
            .hexdigest()[:10]
        add_object_to_db_if_not_exitst(long_url, short_url, max_clicks)
        return render(request, 'show_short_url.html', {"short_url": short_url,
                      "full_short_url": 'cutandgo.com/' + short_url})
    return render(request, 'add_new_url.html')


@logger.catch
def redirect_view(request, following_pattern):
    """Redirect you to long_url via short_url pattern"""
    logger.debug('object getting')
    url = get_object_or_404(URL, short_url=following_pattern)
    click(url)
    max_clicks_check(url)
    print(redirect('http://' + url.long_url))
