# Generated by Django 3.1.6 on 2021-11-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0008_auto_20211129_1024"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
    ]
