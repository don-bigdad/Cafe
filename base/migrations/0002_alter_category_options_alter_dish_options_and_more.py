# Generated by Django 4.1 on 2022-08-06 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',), 'verbose_name': 'Блюда', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('name',), 'verbose_name': 'События', 'verbose_name_plural': 'События'},
        ),
        migrations.AddField(
            model_name='dish',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='dish',
            index_together={('id', 'slug')},
        ),
    ]
