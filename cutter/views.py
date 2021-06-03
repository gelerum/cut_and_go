from hashlib import sha256

from .models import URL
from .forms import URLInput
from django.shortcuts import render, redirect, get_object_or_404


def input_form(request):
    if request.method == 'POST':
        form = URLInput(request.POST)
        if form.is_valid():
            getted_url = form.cleaned_data["full_url"]
            quantity_clicks = form.cleaned_data["max_clicks"]
            until_date = form.cleaned_data["until_date"]
            transformed_url = 'http://' + getted_url
            maked_url = sha256((transformed_url + str(quantity_clicks)).encode()).hexdigest()[:10]
            try:
                URL.objects.get(short_url=maked_url)
            except URL.DoesNotExist:
                URL(full_url=transformed_url, short_url=maked_url,
                    max_clicks=quantity_clicks, until_date=until_date).save()
            return render(request, 'cutter/print_link.html',
                          {'url': '128.0.0.1:800/' + maked_url,
                           'link': maked_url})

    else:
        form = URLInput()
    return render(request, 'cutter/input_form.html', {'form': form})


def redirect_view(request, getted_short_url):
    url = get_object_or_404(URL, short_url=getted_short_url)
    url.click()
    url.clicks_check()
    return redirect(url.full_url)
