# Generated by Django 4.1 on 2022-08-07 17:03

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_specials_pozition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to=base.models.Galery.get_date_name)),
            ],
            options={
                'verbose_name': 'Фотографии',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
