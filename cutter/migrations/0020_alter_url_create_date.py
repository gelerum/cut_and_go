# Generated by Django 3.2.4 on 2021-06-03 14:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0019_alter_url_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 5, 21, 324104, tzinfo=utc)),
        ),
    ]
