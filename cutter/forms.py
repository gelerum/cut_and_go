from django import forms


class URLInput(forms.Form):
    full_url = forms.CharField(label='full_url')
    max_clicks = forms.IntegerField(label='max_clicks')
    until_date = forms.DateField(label='untill_date')
