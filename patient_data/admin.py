from django.contrib import admin
from .models import Doctor,Patient,Record,Career

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Career)