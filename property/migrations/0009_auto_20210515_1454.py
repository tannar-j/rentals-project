# Generated by Django 3.2 on 2021-05-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210515_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='property',
            name='image9',
        ),
    ]
