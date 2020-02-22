from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Doctor,Patient

def patient_view(request):
    records = Record.objects.all()
    return render(request, 'patient_view.html',{'records':records})