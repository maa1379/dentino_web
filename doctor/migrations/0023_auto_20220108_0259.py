# Generated by Django 3.1.6 on 2022-01-08 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0018_auto_20220108_0259'),
        ('doctor', '0022_auto_20220108_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='clinic.clinic'),
        ),
    ]
