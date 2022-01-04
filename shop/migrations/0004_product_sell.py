# Generated by Django 3.1.6 on 2021-12-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_category_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="sell",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]