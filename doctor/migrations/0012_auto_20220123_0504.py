# Generated by Django 3.1.6 on 2022-01-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20220123_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='ID_photo',
            field=models.FileField(blank=True, null=True, upload_to='images/doctor/ID_photo/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='parvaneh_tebabat',
            field=models.FileField(blank=True, null=True, upload_to='images/doctor/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile',
            field=models.FileField(blank=True, null=True, upload_to='images/doctor/profile/'),
        ),
    ]
