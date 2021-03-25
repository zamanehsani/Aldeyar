# Generated by Django 3.1.7 on 2021-03-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0012_auto_20210319_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('month', models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', ' April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=150, null=True)),
                ('Pay', models.DecimalField(decimal_places=3, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Staff Salary',
            },
        ),
    ]