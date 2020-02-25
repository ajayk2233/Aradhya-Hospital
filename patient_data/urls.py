from . import views
from django.urls import path

urlpatterns = [
    path('',views.patient_view,name='patient_view'),
    path('details/<int:id>/',views.details,name='details'),
    path('p_records/<int:id>/',views.p_records,name='p_record'),
    path('d_records/<int:id>/',views.d_records,name='d_record'),
    path('patient_personal_details/',views.patient_personal_details,name='patient_personal_details'),
    path('patient_personal_details/<str:col_name>',views.patient_personal_details,name='patient_personal_details'),
# Patient Personal Details Sort by Ascending Order
    path('patient_personal_order_by/<str:col_name>',views.patient_personal_order_by,name='patient_personal_order_by'),
    path('doctor_personal_details/',views.doctor_personal_details,name='doctor_personal_details'),
    path('collection/',views.collection,name='collection'),
# Career Option
    path('career/',views.career,name='career'),
]