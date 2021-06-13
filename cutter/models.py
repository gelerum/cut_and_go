from django.db import models


class URL(models.Model):
    """Standart project model"""
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=10, default='')
