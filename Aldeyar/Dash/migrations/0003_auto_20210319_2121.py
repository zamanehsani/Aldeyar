# Generated by Django 3.1.7 on 2021-03-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0002_auto_20210319_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bread_package',
        ),
    ]