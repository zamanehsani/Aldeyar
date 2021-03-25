# Generated by Django 3.1.7 on 2021-03-24 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dash', '0015_staff_salary_pay_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]