from django import forms

from doctor.models import Discount

from .models import Clinic, Service


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ("percent", "expertise")
        labels = {"percent": "درصد تخفیف", "expertise": "تخصص"}


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
            "telegram",
            "instagram",
            "parvaneh_clinic",
            "parvaneh_masole",
            "notification",
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
            "image3": "تصویر کلینیک",
            "description": "درباه کلینیک",
            "telegram": "تلگرام",
            "whatsapp": "واتساپ",
            "parvaneh_masole": "پروانه مسول",
            "parvaneh_clinic": "پروانه کلینیک",
            "notification": "شماره اطلاع رسانی",
        }


#
# class ClinicFilter(django_filters.FilterSet):
#     class Meta:
#         model = Clinic
#         fields = ['name']
