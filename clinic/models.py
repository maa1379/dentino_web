from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from location.models import Zone
from partial.models import Company

phone_regex = RegexValidator(
    regex=r"^\d{11}$",
    message=(
        "Phone number must be entered in the format:"
        " '9137866088'. 10 digits allowed."
    ),
)


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Clinic(models.Model):
    TYPE = (
        ("کلینیک", "کلینیک"),
        ("مطب", "مطب"),
        ("لابراتوار", "لابراتوار"),
        ("رادیوگرافی", "رادیوگرافی"),
    )
    name = models.CharField(max_length=125)
    logo = models.ImageField(upload_to="image/clinic")
    address = models.CharField(max_length=450)
    instagram = models.CharField(max_length=125, null=True, blank=True)
    whats_up = models.URLField(max_length=125, null=True, blank=True)
    telegram = models.URLField(max_length=125, null=True, blank=True)
    phone_number = models.TextField()
    description = models.TextField()
    image1 = models.ImageField(upload_to="image/clinic", blank=True)
    image2 = models.ImageField(upload_to="image/clinic", blank=True)
    image3 = models.ImageField(upload_to="image/clinic", blank=True)
    location = models.ForeignKey(Zone, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company, related_name="clinic")
    type = models.CharField(max_length=12, choices=TYPE, null=True, blank=True)
    verified = models.BooleanField(default=False)
    contracted = models.BooleanField(default=False)
    parvaneh_clinic = models.ImageField(
        upload_to="images/clinic/", null=True, blank=True
    )
    parvaneh_masole = models.ImageField(
        upload_to="images/clinic/", null=True, blank=True
    )

    # parvaneh_masole=models.ImageField(upload_to="images/clinic/")
    # city=models.ForeignKey("Location",on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     g = geocoder.mapbox(self.address, key=mapbox_access_token)
    #     g = g.latlng  # returns => [lat, long]
    #     self.lat = g[0]
    #     self.long = g[1]
    #     return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Test(models.Model):
    message = models.CharField(max_length=125, blank=True, null=True)
    From = models.CharField(max_length=125, blank=True, null=True)
    To = models.CharField(max_length=125, blank=True, null=True)
