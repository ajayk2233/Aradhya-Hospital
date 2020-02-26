from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Doctor,Patient,Career
from .forms import RecordForm,DoctorForm,PatientForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create OPD Record
class CreateRecord(CreateView):
    form_class = RecordForm
    template_name = 'create_patient/create_record.html'
    success_url = '/patient_view/'
# Update OPD Record
class UpdateRecord(UpdateView):
    form_class = RecordForm
    template_name = 'create_patient/create_record.html'
    success_url = '/patient_view/'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Record.objects.filter(pk=id)

# Create Patient Record
class CreatePatient(CreateView):
    form_class = PatientForm
    template_name = 'create_patient/create_patient.html'
    success_url = '/patient_view/patient_personal_details/'
# Update Patient Record
class UpdatePatient(UpdateView):
    form_class = PatientForm
    template_name = 'create_patient/create_patient.html'
    success_url = '/patient_view/patient_personal_details/'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Patient.objects.filter(pk=id)