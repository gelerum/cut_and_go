# Generated by Django 3.2.4 on 2021-06-07 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0029_alter_url_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='create_date',
        ),
        migrations.AddField(
            model_name='url',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 7, 5, 34, 2, 17385, tzinfo=utc)),
        ),
    ]
