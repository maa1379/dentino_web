from django.contrib import admin

from .models import Company, Complaint, Prescriptions, Price,DoctorDictionary,DoctorDictionaryCategory

# Register your models here.
admin.site.register(Prescriptions)
admin.site.register(Company)
admin.site.register(Price)
admin.site.register(Complaint)
admin.site.register(DoctorDictionary)
admin.site.register(DoctorDictionaryCategory)
