from django import forms

from .models import Common_Course


class CommenCourseForm(forms.ModelForm):
    class Meta:
        model = Common_Course
        fields = ("image", "title", "source", "description", "video")
        labels = {
            "image": "تصویر",
            "title": "عنوان",
            "source": "منبع",
            "description": "توضیحات",
            "video": "ویدیو",
        }
