# Generated by Django 3.1.6 on 2022-01-10 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0018_auto_20220108_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='notification',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.", regex='^\\d{11}$')]),
        ),
    ]