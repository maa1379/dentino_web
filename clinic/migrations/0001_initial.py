# Generated by Django 3.1.6 on 2022-01-11 11:40

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("partial", "__first__"),
        ("location", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clinic",
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
                ("name", models.CharField(max_length=125)),
                ("logo", models.ImageField(upload_to="image/clinic")),
                ("address", models.CharField(max_length=450)),
                ("instagram", models.CharField(blank=True, max_length=125, null=True)),
                ("whats_up", models.URLField(blank=True, max_length=125, null=True)),
                ("telegram", models.URLField(blank=True, max_length=125, null=True)),
                ("phone_number", models.TextField()),
                ("description", models.TextField()),
                ("image1", models.ImageField(blank=True, upload_to="image/clinic")),
                ("image2", models.ImageField(blank=True, upload_to="image/clinic")),
                ("image3", models.ImageField(blank=True, upload_to="image/clinic")),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("کلینیک", "کلینیک"),
                            ("مطب", "مطب"),
                            ("لابراتوار", "لابراتوار"),
                            ("رادیوگرافی", "رادیوگرافی"),
                        ],
                        max_length=12,
                        null=True,
                    ),
                ),
                ("verified", models.BooleanField(default=False)),
                ("contracted", models.BooleanField(default=False)),
                (
                    "parvaneh_clinic",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/clinic/"
                    ),
                ),
                (
                    "parvaneh_masole",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/clinic/"
                    ),
                ),
                (
                    "notification",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.",
                                regex="^\\d{11}$",
                            )
                        ],
                    ),
                ),
                (
                    "company",
                    models.ManyToManyField(related_name="clinic", to="partial.Company"),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="location.zone"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=125)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                ("message", models.CharField(blank=True, max_length=125, null=True)),
                ("From", models.CharField(blank=True, max_length=125, null=True)),
                ("To", models.CharField(blank=True, max_length=125, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Winner",
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
                ("expertise", models.CharField(max_length=150)),
                ("discount", models.IntegerField()),
                ("created", models.DateField(auto_now_add=True)),
                ("used", models.BooleanField(default=False)),
                ("clinic", models.CharField(max_length=125)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
