# Generated by Django 3.1.6 on 2021-11-12 20:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clinic", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=100)),
                ("family", models.CharField(max_length=100)),
                (
                    "national_code",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.",
                                regex="^\\d{10}$",
                            )
                        ],
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.",
                                regex="^\\d{10}$",
                            )
                        ],
                    ),
                ),
                ("ID_photo", models.ImageField(upload_to="images/doctor/ID_photo/")),
                ("profile", models.ImageField(upload_to="images/doctor/profile/")),
                (
                    "medical_code",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.",
                                regex="^\\d{10}$",
                            )
                        ],
                    ),
                ),
                ("full_name", models.CharField(max_length=250)),
                ("bio", models.TextField()),
                ("age", models.PositiveIntegerField()),
                (
                    "clinic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor",
                        to="clinic.clinic",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expertise",
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
                ("image", models.ImageField(blank=True, upload_to="images/Expertise/")),
            ],
        ),
        migrations.CreateModel(
            name="VisitTime",
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
                ("date", models.DateTimeField()),
                ("start_time", models.DateTimeField()),
                ("finish_time", models.DateTimeField()),
                ("is_reserved", models.BooleanField(default=False)),
                ("doctor", models.ManyToManyField(to="doctor.Doctor")),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="expertise",
            field=models.ManyToManyField(related_name="doctor", to="doctor.Expertise"),
        ),
    ]
