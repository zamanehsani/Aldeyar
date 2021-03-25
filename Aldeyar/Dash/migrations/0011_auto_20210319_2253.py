# Generated by Django 3.1.7 on 2021-03-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0010_expenses_unit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('totol_price', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
            options={
                'verbose_name_plural': 'Staff Expenses',
            },
        ),
        migrations.AlterField(
            model_name='expenses',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('Piece', 'Piece'), ('KG', 'KG'), ('Liter', 'Liter'), ('Gallon', ' Gallon'), ('Package', 'Package')], max_length=150, null=True),
        ),
    ]