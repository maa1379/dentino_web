from django.contrib.auth import get_user_model
from django.db import models

# from clinic.models import Clinic
import doctor.models

user = get_user_model()


# class Patient(models.Model):
# name = models.CharField(max_length=125)
# family = models.CharField(max_length=125)
# phone_number = models.CharField(max_length=11)
# national_code = models.CharField(max_length=125)

# def __str__(self):
# return f'{self.name}-{self.family}'


class Reservation(models.Model):
    name = models.CharField(max_length=125, null=True)
    family = models.CharField(max_length=125, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    national_code = models.CharField(max_length=125, null=True)
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="reserve", blank=True, null=True
    )
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="ali")
    doctor = models.ForeignKey(
        doctor.models.Doctor, on_delete=models.CASCADE, related_name="reserve"
    )
    # clinic=models.ForeignKey()
    day = models.CharField(max_length=125, null=True)
    time = models.CharField(max_length=125, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"reserve {self.doctor} at {self.day}-{self.time}"
