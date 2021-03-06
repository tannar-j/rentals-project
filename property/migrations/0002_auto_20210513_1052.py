# Generated by Django 3.2 on 2021-05-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='area',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='baths',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
