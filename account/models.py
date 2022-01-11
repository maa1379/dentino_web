import random

from django.contrib.auth.models import AbstractBaseUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save

from clinic.models import Clinic

# from .managers import MyUserManager

phone_regex = RegexValidator(
    regex=r"^\d{10}$",
    message=(
        "Phone number must be entered in the format:"
        " '9137866088'. 10 digits allowed."
    ),
)
insurance_regex = RegexValidator(
    regex=r"^\d{10}$",
    message=(
        "insurance  must be entered in the format:" " '12345678'. 8 digits allowed."
    ),
)


def UniqueGenerator(length=8):
    source = "0123456789"
    result = ""
    for _ in range(length):
        result += source[random.randint(0, length)]
    return result


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    national_code = models.IntegerField(unique=True, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    family = models.CharField(max_length=125, blank=True, null=True)
    is_done = models.BooleanField(default=False)
    is_clinic = models.BooleanField(default=False)
    clinic = models.OneToOneField(
        Clinic, on_delete=models.CASCADE, blank=True, null=True
    )
    referral_code = models.CharField(max_length=8, default=UniqueGenerator)
    invite_code = models.CharField(max_length=8, null=True, blank=True)

    @property
    def invited_user_count(self):
        user_referral_code = self.referral_code
        all_user = Profile.objects.filter(invite_code=user_referral_code).count()
        return all_user

    @property
    def user_score(self):
        score = self.invited_user_count*10
        return score
    #
    #
    # def generate_verification_code(self):
    #     return base64.urlsafe_b64encode(uuid.uuid1())[:7]

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.referral_code = self.generate_verification_code()
    #     elif not self.verification_code:
    #         self.referral_code = self.generate_verification_code()
    #
    #     return super(Profile, self).save(*args, **kwargs)

    # is_doctor = models.BooleanField(default=False,null=True)
    # is_active = models.BooleanField(default=True,null=True)
    # is_admin = models.BooleanField(default=False,null=True)
    # objects = MyUserManager()
    # USERNAME_FIELD = "phone_number"

    # def __str__(self):
    #     return f"{self.name}-{self.family}"
    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin


#
# class Photo_History(models.Model):
#     picture = models.ImageField(upload_to="images/photo_history")
#     date = models.DateField()
#     models.ForeignKey(User, on_delete=models.CASCADE)


def save_profile(sender, **kwargs):
    if kwargs["created"]:
        p1 = Profile(user=kwargs["instance"])
        p1.save()


post_save.connect(save_profile, sender=User)


class Code(models.Model):
    number = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=11)
