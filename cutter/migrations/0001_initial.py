# Generated by Django 3.1.7 on 2021-06-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.CharField(max_length=200)),
                ('short_url', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
