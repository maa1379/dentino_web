from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
phone_regex = RegexValidator(
    regex=r"^\d{10}$",
    message=(
        "Phone number must be entered in the format:"
        " '9137866088'. 10 digits allowed."
    ),
)


class Slider(models.Model):
    title = models.CharField(max_length=125)
    picture = models.ImageField(upload_to="images/sliders/%Y/%m")


class SiteConfig(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    icon = models.ImageField(upload_to="images/icon/")

    def __str__(self):
        return self.title


class About_Us(models.Model):
    content = models.TextField()


class Contact_Us(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
