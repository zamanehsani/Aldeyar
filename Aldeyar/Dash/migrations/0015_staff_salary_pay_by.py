# Generated by Django 3.1.7 on 2021-03-23 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dash', '0014_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_salary',
            name='pay_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]
