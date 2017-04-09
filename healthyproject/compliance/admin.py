from django.contrib import admin
from compliance.models import Doctor, Patient, Initial
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Initial)
