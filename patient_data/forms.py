from .models import Record,Patient,Doctor,Career
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'patient_name' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_address': forms.TextInput(attrs={'rows':15,'class':'form-control'}),
            'patient_city' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_contact': forms.TextInput(attrs={'class':'form-control'}),
            'patient_age': forms.TextInput(attrs={'class':'form-control'}),
            'patient_ID': forms.TextInput(attrs={'class':'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'doctor_name' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_address': forms.TextInput(attrs={'rows':15,'class':'form-control'}),
            'doctor_city' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_contact': forms.TextInput(attrs={'class':'form-control'}),
            'doctor_age': forms.TextInput(attrs={'class':'form-control'}),
            'doctor_ID': forms.TextInput(attrs={'class':'form-control'}),
        }

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'doctor' : forms.Select(attrs={'class':'form-control'}),
            'patient': forms.Select(attrs={'class':'form-control'}),
            'weight' : forms.TextInput(attrs={'class':'form-control'}),
            'disease': forms.Textarea(attrs={'class':'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'suggestion': forms.Textarea(attrs={'class':'form-control'}),
            'fees': forms.TextInput(attrs={'class':'form-control'}),
        }