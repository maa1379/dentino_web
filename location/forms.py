from django import forms

from .models import City, Province, Zone


class LocationForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ("name",)

        labels = {
            "name": "منطقه",
        }


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ("name", "city")

        labels = {
            "name": "منطقه",
            "city": "شهر",
        }


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ("name",)

        labels = {
            "name": "استان",
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ("name", "province")

        labels = {
            "name": "شهر",
            "province": "استان",
        }
