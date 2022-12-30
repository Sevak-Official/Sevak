from django.contrib import admin
from .models import Hospital,Doctor,Patient
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)