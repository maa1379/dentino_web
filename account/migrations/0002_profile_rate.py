# Generated by Django 3.1.6 on 2022-01-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rate',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]