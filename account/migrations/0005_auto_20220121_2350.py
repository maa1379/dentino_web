# Generated by Django 3.1.6 on 2022-01-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220121_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('عادی', 'عادی'), ('کلینیک', 'کلینیک'), ('فروشگاه', 'فروشگاه')], default='عادی', max_length=10),
        ),
    ]
