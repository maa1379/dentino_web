import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("logo", models.ImageField(upload_to="")),
                ("address", models.CharField(max_length=450)),
                ("lat", models.FloatField(blank=True, null=True)),
                ("long", models.FloatField(blank=True, null=True)),
                ("instagram", models.URLField()),
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
            name="Phone_number",
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
                (
                    "number",
                    models.CharField(
                        max_length=11,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '9137866088'. 10 digits allowed.",
                                regex="^\\d{11}$",
                            )
                        ],
                    ),
                ),
                (
                    "clinic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clinic.clinic"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="clinic",
            name="services",
            field=models.ManyToManyField(related_name="clinic", to="clinic.Service"),
        ),
    ]
