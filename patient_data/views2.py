from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Doctor,Patient,Career
from .forms import RecordForm,DoctorForm,PatientForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create OPD Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class CreateRecord(CreateView):
    form_class = RecordForm
    template_name = 'create_patient/create_record.html'
    success_url = '/patient_view/'

# Update OPD Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class UpdateRecord(UpdateView):
    form_class = RecordForm
    template_name = 'create_patient/create_record.html'
    success_url = '/patient_view/'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Record.objects.filter(pk=id)

# Create Patient Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class CreatePatient(CreateView):
    form_class = PatientForm
    template_name = 'create_patient/create_patient.html'
    success_url = '/patient_view/patient_personal_details/'

# Update Patient Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class UpdatePatient(UpdateView):
    form_class = PatientForm
    template_name = 'create_patient/create_patient.html'
    success_url = '/patient_view/patient_personal_details/'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Patient.objects.filter(pk=id)

# Create Doctor Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class CreateDoctor(CreateView):
    form_class = DoctorForm
    template_name = 'create_patient/create_doctor.html'
    success_url = '/patient_view/doctor_personal_details/'

# Update Patient Record
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class UpdateDoctor(UpdateView):
    form_class = DoctorForm
    template_name = 'create_patient/create_doctor.html'
    success_url = '/patient_view/doctor_personal_details/'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Doctor.objects.filter(pk=id)