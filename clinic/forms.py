from django import forms

from .models import Clinic, Service


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
        fields = ("name", "logo", "address", "instagram", "location", "company","type","image1","image2","image3","description","phone_number")
        labels = {
            "name": "عنوان",
            "logo": "لوگو",
            "address": "آدرس",
            "phone_number": "شماره تماس",
            "instagram": "اینستاگرام",
            "location": "منطقه",
            "company": "شرکت های طرف قراداد",
            "type": "نوع مرکز",
            'image1':"تصویر کلینیک",
            'image2':"تصویر کلینیک",
            'image3':"تصویر کلینیک",
            'description':"درباه کلینیک",
            'phone_number':"شماره های تماس",
        }


#
# class ClinicFilter(django_filters.FilterSet):
#     class Meta:
#         model = Clinic
#         fields = ['name']
