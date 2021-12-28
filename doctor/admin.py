from django.contrib import admin

from doctor.models import VisitTime

from .models import Doctor, Expertise, Insurance, VisitTime ,DoctorDate

admin.site.register(Doctor)

admin.site.register(Expertise)
admin.site.register(Insurance)
admin.site.register(DoctorDate)

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin
from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter

#
# class BarAdmin(admin.ModelAdmin):
#     list_filter = (
#         ('date', JDateFieldListFilter),
#     )
#
#
# admin.site.register(Bar, BarAdmin)


class BarTimeAdmin(admin.ModelAdmin):
    list_filter = (("date", JDateFieldListFilter),)


admin.site.register(VisitTime, BarTimeAdmin)
