from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "price",
            "image",
            "image2",
            "image3",
            "image4",
            "description",
            "phone_number",
            "address",
            "category",
            "sell",
        )
        labels = {
            "name": "نام محصول",
            "description": "توضیحات محصول",
            "image": "تصویر شماره یک",
            "image2": "تصویر شماره دو",
            "image3": "تصویر شماره سه",
            "image4": "تصویر شماره چهار",
            "phone_number": "شماره تماس",
            "address": "آدرس",
            "price": "قیمت",
            "category": "دسته بندی",
            "sell": "قیمت ما",
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("title", "icon")

        labels = {
            "title": "عنوان",
            "icon": "آیکون",
        }
