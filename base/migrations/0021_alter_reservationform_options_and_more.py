# Generated by Django 4.1 on 2022-08-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_reservationform_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservationform',
            options={'ordering': ('-timeadd', '-is_processed')},
        ),
        migrations.AddField(
            model_name='reservationform',
            name='timeadd',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
