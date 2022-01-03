from django import forms


class UserSignupForm(forms.Form):
    phone_number = forms.CharField(max_length=11, label="شماره تماس")
    national_code = forms.CharField(max_length=11, label="کد ملی")
    name = forms.CharField(max_length=125, label="نام")
    family = forms.CharField(max_length=125, label="نام خانوادگی")
