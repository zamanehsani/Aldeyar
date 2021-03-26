# Generated by Django 3.1.7 on 2021-03-26 11:40

import Dash.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0022_auto_20210326_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=Dash.models.upload_location, verbose_name='Upload a square picture of yourself.'),
        ),
    ]
