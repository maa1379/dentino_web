import datetime

from django.core.validators import (RegexValidator)
from django.db import models

from clinic.models import Clinic

regex = RegexValidator(
    regex=r"^\d{10}$",
    message=(
        "Phone number must be entered in the format:"
        " '9137866088'. 10 digits allowed."
    ),
)


class Insurance(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to="image/insurance")

    def __str__(self):
        return self.name


class Expertise(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to="images/Expertise/", blank=True)

    def __str__(self):
        return self.title


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    national_code = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    ID_photo = models.ImageField(upload_to="images/doctor/ID_photo/")
    profile = models.ImageField(upload_to="images/doctor/profile/")
    medical_code = models.CharField(max_length=11)
    # service = models.ForeignKey(Service, on_delete=models.CASCADE)
    insurance = models.ManyToManyField(Insurance)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="doctor", null=True, blank=True)
    expertise = models.ManyToManyField(Expertise, related_name="doctor")
    full_name = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField()
    star = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.family

    # def __str__(self):
    #     return f"{self.name}-{self.family}"
    #
    def save(self):
        self.full_name = f"{self.name} {self.family}"
        return super(Doctor, self).save()


from django_jalali.db import models as jmodels


class VisitTime(models.Model):
    CHOICE = (
        ("شنبه", "شنبه"),
        ("یکشنبه", "یکشنبه"),
        ("دوشنبه", "دوشنبه"),
        ("سه شنبه", "سه شنبه"),
        ("چهارشنبه", "چهارشنبه"),
        ("پنجشنبه", "پنجشنبه"),
        ("جمعه", "جمعه"),
    )
    day = models.CharField(max_length=10, choices=CHOICE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    date = jmodels.jDateField()
    objects = jmodels.jManager()
    # objects = jmodels.jManager()
    start_time = models.DateTimeField(default=datetime.datetime.now)
    finish_time = models.DateTimeField(default=datetime.datetime.now)
    start_time2 = models.DateTimeField(default=datetime.datetime.now)
    finish_time2 = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "ali"


class DoctorDate(models.Model):
    name=models.CharField(max_length=20)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.ForeignKey(VisitTime,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
