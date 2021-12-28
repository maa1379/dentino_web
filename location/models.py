from django.db import models
from mptt.models import MPTTModel


class Province(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    province = models.ForeignKey(
        "Province",
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField()
    city = models.ForeignKey(
        "City",
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
