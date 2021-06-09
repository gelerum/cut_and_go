from django.db import models
from django.utils.timezone import now


class URL(models.Model):
    """Standart project model"""
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=10, default='')
    max_clicks = models.IntegerField(null=True, default=0)
    count_clicks = models.IntegerField(default=0)
