from . import views,views2
from django.urls import path

urlpatterns = [
# 1 - OPD
# Show OPD Record
    path('',views.patient_view,name='patient_view'),
# OPD Single Patient Detail Record
    path('details/<int:id>/',views.details,name='details'),
# Create OPD Record
    path('create_record/',views2.CreateRecord.as_view(),name='create_record'),
# Update OPD Record
    path('update_record/<int:pk>',views2.UpdateRecord.as_view(),name='update_record'),
# Delete OPD Record
    path('delete_record/<int:pk>/',views2.DeleteRecord.as_view(),name='delete_record'),

# 2 Patient
# Show Patients Personal Record
    path('patient_personal_details/',views.patient_personal_details,name='patient_personal_details'),
# Show Patient Single Personal Record
    path('p_records/<int:id>/',views.p_records,name='p_record'),
# Create Patient Personal Record
    path('create_patient/',views2.CreatePatient.as_view(),name='create_patient'),
# Update Patient Personal Record
    path('update_patient/<int:pk>',views2.UpdatePatient.as_view(),name='update_patient'),
# ShowPatients Personal Record order by Column Name/Descending Order
    path('patient_personal_details/<str:col_name>',views.patient_personal_details,name='patient_personal_details'),
# Show Patient Personal Details Sort by Ascending Order
    path('patient_personal_order_by/<str:col_name>',views.patient_personal_order_by,name='patient_personal_order_by'),
# Delete OPD Record
    path('delete_patient/<int:pk>/',views2.DeletePatient.as_view(),name='delete_patient'),

# 3 Doctor
# Show Doctor Personal Records
    path('doctor_personal_details/',views.doctor_personal_details,name='doctor_personal_details'),
# Show Doctor Single Personal Record
    path('d_records/<int:id>/',views.d_records,name='d_record'),
# Create Doctor Personal Record
    path('create_doctor/',views2.CreateDoctor.as_view(),name='create_doctor'),
# Update Doctor Personal Record
    path('update_doctor/<int:pk>',views2.UpdateDoctor.as_view(),name='update_doctor'),
# Delete Doctor Personal Record
    path('delete_doctor/<int:pk>',views2.DeleteDoctor.as_view(),name='delete_doctor'),

# Daily/Selected Duration Collection
    path('collection/',views.collection,name='collection'),
# Career Option
    path('career/',views.career,name='career'),
# Career Record List
    path('career_record/<int:id>/',views.career_record,name='career_record'),
    path('career_record/',views.career_record,name='career_record'),
    path('delete_career/<int:id>/',views.delete_career,name='delete_career'),
# Contact Option
    path('contactus/',views.contactus,name='contactus'),
# Contact Record List
    path('contactus_record/',views.contactus_record,name='contactus_record'),
    path('contactus_record/<int:id>/',views.contactus_record,name='contactus_record'),
    path('delete_contactus/<int:id>/',views.delete_contactus,name='delete_contactus'),
    
]