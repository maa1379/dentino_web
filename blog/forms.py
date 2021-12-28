from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "author",
            "title",
            "description",
            "image",
            "tags",
            "status",
            "publish_time",
        )
        labels = {
            "author": "نویسنده",
            "title": "عنوان",
            "description": "متن",
            "image": "تصویر",
            "tags": "تگ ها",
            "status": "وضعیت",
            "publish_time": "زمان انتشار",
        }
