# Generated by Django 3.1 on 2020-08-06 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_1', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='idade',
        ),
    ]
