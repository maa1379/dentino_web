from django.contrib import admin

from .models import City, Province, Zone

# Register your models here.
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Zone)
