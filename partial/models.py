from django.contrib.auth import get_user_model
from django.db import models

#
# from doctor.models import Doctor
# from clinic.models import Clinic
user = get_user_model()


# Create your models here.
class Prescriptions(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/prescriptions/")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Insurance(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/insurance/")


class Company(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/company/")

    def __str__(self):
        return self.title


class Price(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()


class Complaint(models.Model):
    text = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="user_compliment")
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_compliment")
    # clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE,related_name="clinic_compliment")


class DoctorDictionary(models.Model):
    word = models.CharField(max_length=255)
    meaning = models.TextField()
    logo = models.ImageField(upload_to="doctor/images/dictonary/", null=True, blank=True)
    category = models.ForeignKey("DoctorDictionaryCategory", on_delete=models.CASCADE, related_name="dict", blank=True,
                                 null=True)

    def __str__(self):
        return self.word


class ImageOfDict(models.Model):
    image = models.ImageField(upload_to="images/")
    dict = models.ForeignKey(DoctorDictionary, on_delete=models.CASCADE, related_name="dict")

    def __str__(self):
        return f"{self.image} of {self.dict}"


class DoctorDictionaryCategory(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
