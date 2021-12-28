from django import forms

from .models import Slider


class PanelLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام کاربری"}
        ),
        label="نام کاربری",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "رمز عبور"}
        ),
        label="رمز عبور",
    )


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ("title", "picture")
        labels = {
            "title": "عنوان",
            "picture": "تصویر",
        }
