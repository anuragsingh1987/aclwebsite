# Generated by Django 3.1.5 on 2021-01-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_event_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_slug',
            field=models.SlugField(default='test', max_length=40),
        ),
    ]
