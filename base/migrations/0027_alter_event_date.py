# Generated by Django 4.1 on 2022-08-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_event_options_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
