from django.shortcuts import render,HttpResponse,redirect

def patient_view(request):
    return render(request, 'patient_view.html')