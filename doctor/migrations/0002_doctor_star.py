# Generated by Django 3.1.6 on 2021-11-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="star",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
