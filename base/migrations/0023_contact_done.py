# Generated by Django 4.1 on 2022-08-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_contact_alter_reservationform_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
