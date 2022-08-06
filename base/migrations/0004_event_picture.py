# Generated by Django 4.1 on 2022-08-06 12:30

import base.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_event_options_event_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=base.models.Event.get_date_name),
            preserve_default=False,
        ),
    ]