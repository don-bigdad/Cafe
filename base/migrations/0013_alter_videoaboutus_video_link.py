# Generated by Django 4.1 on 2022-08-09 20:46

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_videoaboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoaboutus',
            name='video_link',
            field=models.FileField(upload_to=base.models.VideoAboutUs.video_name),
        ),
    ]