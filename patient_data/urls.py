from . import views
from django.urls import path

urlpatterns = [
    path('',views.patient_view,name='patient_view'),
]
