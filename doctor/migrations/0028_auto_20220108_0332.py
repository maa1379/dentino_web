# Generated by Django 3.1.6 on 2022-01-08 11:32

from django.db import migrations

import doctor.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0027_auto_20220108_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=doctor.models.IntegerRangeField(),
        ),
    ]