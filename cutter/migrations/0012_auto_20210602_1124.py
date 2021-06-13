from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0011_remove_url_temporality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='clicks',
            new_name='count_clicks',
        ),
        migrations.AddField(
            model_name='url',
            name='max_clicks',
            field=models.IntegerField(default=0),
        ),
    ]
