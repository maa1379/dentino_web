# Generated by Django 3.1.6 on 2021-12-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0010_clinic_is_clinic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clinic",
            name="is_clinic",
        ),
        migrations.AddField(
            model_name="clinic",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("کلینیک", "کلینیک"), ("مطب", "مطب")],
                max_length=12,
                null=True,
            ),
        ),
    ]
