from django.contrib import admin

from .models import Clinic, Service, Winner

admin.site.register(Clinic)
admin.site.register(Service)
admin.site.register(Winner)
