# Generated by Django 3.1.6 on 2021-12-23 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0011_auto_20211222_1058"),
        ("doctor", "0016_auto_20211216_0659"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="clinic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor",
                to="clinic.clinic",
            ),
        ),
    ]
