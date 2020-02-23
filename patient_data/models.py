from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=40)
    doctor_address = models.TextField()
    doctor_city = models.CharField(max_length=30,default='Unknown')
    doctor_contact = models.CharField(max_length=10)
    doctor_age = models.IntegerField()
    doctor_ID = models.IntegerField(unique=True)
    doctor_join_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    patient_name = models.CharField(max_length=40)
    patient_address = models.TextField()
    patient_city = models.CharField(max_length=30,default='Unknown')
    patient_contact = models.CharField(max_length=10)
    patient_age = models.IntegerField()
    patient_ID = models.IntegerField(unique=True)
    patient_registration_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.patient_name


class Record(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    weight = models.IntegerField()
    disease = models.TextField()
    diagnosis = models.TextField()
    suggestion = models.TextField()
    fees = models.IntegerField()
    date_created = models.DateField(auto_now_add=True,blank=True,null=True)