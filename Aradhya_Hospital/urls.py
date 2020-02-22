from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient_view',include('patient_data.urls')),
    path('',views.home,name='home'),
]
