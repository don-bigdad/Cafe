# Generated by Django 4.1 on 2022-08-10 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_contact_done'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-done',)},
        ),
    ]
