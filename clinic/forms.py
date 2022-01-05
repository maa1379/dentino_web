from django import forms

from doctor.models import Discount
from .models import Clinic, Service


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ("clinic", "percent", "expertise")
        labels = {"clinic": "مرکز درمانی", "percent": "درصد تخفیف", "expertise": "تخصص"}


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("title",)

        labels = {
            "title": "عنوان",
        }


class ClinicCreateForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = (
            "name",
            "logo",
            "address",
            "instagram",
            "location",
            "company",
            "type",
            "image1",
            "image2",
            "image3",
            "description",
            "phone_number",
            "image4",
            "image5",
            "telegram",
            "instagram",
            'parvaneh_clinic',
            'parvaneh_masole'
        )
        labels = {
            "name": "عنوان",
            "logo": "لوگو",
            "address": "آدرس",
            "phone_number": "شماره تماس",
            "instagram": "اینستاگرام",
            "location": "منطقه",
            "company": "شرکت های طرف قراداد",
            "type": "نوع مرکز",
            "image1": "تصویر کلینیک",
            "image2": "تصویر کلینیک",
            "image4": "تصویر کلینیک",
            "image5": "تصویر کلینیک",
            "description": "درباه کلینیک",
            "telegram": "تلگرام",
            "whatsapp": "واتساپ",
            "parvaneh_masole":"پروانه مسول",
            "parvaneh_clinic":"پروانه کلینیک",
        }


#
# class ClinicFilter(django_filters.FilterSet):
#     class Meta:
#         model = Clinic
#         fields = ['name']
