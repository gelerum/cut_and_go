from hashlib import sha256

from .models import URL
from .services import add_object_to_db_if_not_exitst
from django.shortcuts import render, redirect, get_object_or_404


def add_new_url_view(request):
    """View for start page with form long_url"""
    short_url = ''
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
        short_url = sha256((long_url).encode()) \
            .hexdigest()[:10]
        add_object_to_db_if_not_exitst(long_url, short_url)
        return render(request, 'index.html', {
            'short_url': '127.0.0.1:8000/' + short_url,
        })
    return render(request, 'index.html', {
        'short_url': '',
    })


def redirect_view(request, following_pattern):
    """Redirect you to long_url via short_url pattern"""
    url = get_object_or_404(URL, short_url=following_pattern)
    return redirect('http://' + url.long_url)
