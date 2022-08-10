# Generated by Django 4.1 on 2022-08-10 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_reservationform_alter_videoaboutus_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationform',
            name='date',
            field=models.DateField(max_length=30, validators=[django.core.validators.RegexValidator(message='Invalid date', regex='^(\\d{1,2})([-: .]\\d{1,2})?$')]),
        ),
        migrations.AlterField(
            model_name='reservationform',
            name='number_of_people',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Invalid time', regex='^\\^[1-5][1-9]$$')]),
        ),
    ]
