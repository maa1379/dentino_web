# Generated by Django 3.1.6 on 2021-11-12 20:39

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField()),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="location.location",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
