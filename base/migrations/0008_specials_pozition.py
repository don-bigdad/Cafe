# Generated by Django 4.1 on 2022-08-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_specials_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='specials',
            name='pozition',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
