# Generated by Django 3.1.7 on 2021-03-19 17:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0004_farsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='bread',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farsi',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BBQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bbq_package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Dash.bread')),
            ],
        ),
    ]
