# Generated by Django 3.1.7 on 2021-03-26 10:55

import Dash.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dash', '0020_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True, verbose_name='tell me about yourself')),
                ('phone', models.PositiveIntegerField(blank=True, null=True, verbose_name='what is your phone?')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='where do you live?')),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to=Dash.models.upload_location, verbose_name='Upload a square picture of yourself.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
