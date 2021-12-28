from django import forms

from .models import Company, Prescriptions, Price,DoctorDictionary


class DoctorDictionaryForm(forms.ModelForm):
    class Meta:
        model=DoctorDictionary
        fields=("word","meaning","logo","category")
        labels = {"word": "لغت", "meaning": "معنی","logo":"لوگو","category":"دسته بندی"}




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("title", "image")
        labels = {"title": "نام مجموعه", "image": "لوگو"}


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ("title", "price")

        labels = {"title": "عنوان", "price": "قیمت"}


class Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("title", "image")

        labels = {"title": "نام مجموعه", "image": "لوگو"}


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = (
            "title",
            "description",
            "image",
        )
        labels = {
            "title": "عنوان",
            "description": "توضیحات",
            "image": "تصویر",
        }
