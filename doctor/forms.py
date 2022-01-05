from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from .models import Doctor, Expertise, Insurance, VisitTime


class TestForm(forms.ModelForm):
    class Meta:
        model = VisitTime
        fields = (
            "doctor",
            "day",
        )

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields["date"] = JalaliDateField(
            label=("date"),  # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget
            # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        # self.fields['start_time'] = SplitJalaliDateTimeField(label=('date time'),
        #                                                      widget=AdminSplitJalaliDateTime
        # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )


class VisitTimeForm(forms.ModelForm):
    class Meta:
        model = VisitTime
        fields = (
            "doctor",
            "date",
            "start_time",
            "finish_time",
            "start_time2",
            "finish_time2",
        )
        labels = {
            "doctor": "دکتر",
            "date": "تاریخ",
            "start_time": "شروع شیفت اول",
            "finish_time": "پایان شیفت اول",
            "start_time2": "شروع شیفت دوم",
            "finish_time2": "پایان شیفت دوم",
        }
        widgets = {
            "date": forms.DateInput(attrs={"id": "datepicker"}),
        }
        # from django import forms
        #
        # class DateForm(forms.Form):
        #     date = forms.DateTimeField(
        #         input_formats=['%d/%m/%Y %H:%M'],
        #         widget=forms.DateTimeInput(attrs={
        #             'class': 'form-control datetimepicker-input',
        #             'data-target': '#datetimepicker1'
        #         })
        #     )
        # }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            "name",
            "family",
            "national_code",
            "phone_number",
            "ID_photo",
            "clinic",
            "expertise",
            "profile",
            "age",
            "bio",
            "medical_code",
            "parvaneh_tebabat"
        )

        labels = {
            "name": "نام",
            "family": "نام خانوادگی",
            "national_code": "کد ملی",
            "phone_number": "شماره تماس",
            "ID_photo": "تصویر کد ملی",
            "resume": "رزومه",
            "clinic": "کلینیک ",
            "expertise": "تخصص",
            "profile": "پروفایل",
            "age": "سن",
            "bio": "بیو",
            "medical_code": "کد نظام پزشکی",
            "parvaneh_tebabat": "پروانه طبابت",
        }


class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = {"title", "image"}
        labels = {"title": "عنوان", "image": "تصویر"}


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ("name", "image")

        labels = {"name": "نام بیمه", "image": "لوگو"}
