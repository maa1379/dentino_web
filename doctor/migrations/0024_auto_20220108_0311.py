# Generated by Django 3.1.6 on 2022-01-08 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0023_auto_20220108_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(20)]),
        ),
    ]
