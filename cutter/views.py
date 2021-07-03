import os
from hashlib import sha256

from django.shortcuts import get_object_or_404, redirect, render

from .models import URL
from .services import add_object_to_db_if_not_exitst, url_to_one_kind


def index_view(request):
    """Startpage with form for cutting"""
    short_url = ''
    if request.method == 'POST':
        initial_url = request.POST["initial_url"]
        long_url = url_to_one_kind(initial_url)
        short_url = sha256(long_url.encode()).hexdigest()[:10]
        add_object_to_db_if_not_exitst(long_url, short_url)
        short_url = os.getenv('SITE_URL') + '/' + short_url
    return render(request, 'index.html', {
        'short_url': short_url,
    })


def redirect_view(request, redirect_pattern):
    """Redirect you to long_url via short_url pattern"""
    url = get_object_or_404(URL, short_url=redirect_pattern)
    return redirect('http://' + url.long_url)
