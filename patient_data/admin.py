from django.contrib import admin
from .models import Doctor,Patient,Record,Career,ContactUs

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Career)
admin.site.register(ContactUs)