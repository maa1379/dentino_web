from django import forms

from account.models import Profile


class UserSignupForm(forms.Form):
    phone_number = forms.CharField(max_length=11, label="شماره تماس")
    national_code = forms.CharField(max_length=11, label="کد ملی")
    name = forms.CharField(max_length=125, label="نام")
    family = forms.CharField(max_length=125, label="نام خانوادگی")


class EditProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11)

    class Meta:
        model = Profile
        fields = ("national_code", "name", "family")

        labels = {
            "national_code": "کد ملی",
            "name": "نام",
            "family": "نام خانوادگی",
        }
