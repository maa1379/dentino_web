from django.contrib import admin

from .models import Code, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Code)
