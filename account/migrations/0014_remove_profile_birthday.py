# Generated by Django 3.1.6 on 2022-01-11 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20220110_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
    ]