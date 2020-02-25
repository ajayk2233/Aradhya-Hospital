from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Doctor,Patient,Career

# Show all OPD Record
# def patient_view(request):
#     records = Record.objects.all()
#     return render(request, 'patient_data/patient_view.html',{'records':records})

# OPD Record Filter by Date
def patient_view(request):
    records = Record.objects.all()
    return render(request, 'patient_data/patient_view.html',{'records':records})

# Show all Patient Personal Details
def patient_personal_details(request,col_name=None):
    if col_name is None:
        patient = Patient.objects.all()
        return render(request, 'patient_data/patient_personal_details.html',{'patient':patient})
    else:
        patient = Patient.objects.all().order_by(col_name)
        return render(request, 'patient_data/patient_personal_details.html',{'patient':patient})
# Show all Patient Personal Details order by Age
def patient_personal_order_by(request,col_name):
    patient = Patient.objects.all().order_by(col_name)
    return render(request, 'patient_data/patient_personal_order_by.html',{'patient':patient})

# Show all Doctors Personal Details
def doctor_personal_details(request):
    doctor = Doctor.objects.all()
    return render(request, 'patient_data/doctor_personal_details.html',{'doctor':doctor})
# Show Single OPD Record
def details(request,id):
    details = Record.objects.get(id=id)
    print(id)
    return render(request, 'patient_data/patient_view_details.html',{'details':details})
# Show Single Patient Personal Record
def p_records(request,id):
    p_records = Patient.objects.get(id=id)
    return render(request, 'patient_data/p_records.html',{'record':p_records})
# Show Single Doctor Personal Record
def d_records(request,id):
    d_records = Doctor.objects.get(id=id)
    return render(request, 'patient_data/d_records.html',{'record':d_records})

def collection(request):
    if request.method == 'POST':
        start_date = request.POST.get("date1")
        end_date = request.POST.get('date2')
        cash = 0
        try:
            for i in Record.objects.filter(date_created__range=[start_date, end_date]):
                cash = cash + i.fees
        except:
            return render(request,'collection.html',{'message':'Kindly Enter Valid Date'})
        return render(request,'collection.html',{'cash':cash})
    return render(request,'collection.html',{'message':'Kindly select Date to see collection'})

def career(request):
    if request.method == 'POST':
        job = Career()
        email = request.POST['email']
        job_post = request.POST['job_post']

        for i in  Career.objects.all():
            if i.email == email:
                return render(request, 'career.html',{'message':'You have already Applied with current email id'})
        job.email = email
        job.job_post = job_post
        job.save()
        message = f"Congratulations {job.email} you will shortly get email regarding Job Notification."
        return render(request, 'career.html',{'message':message})
    return render(request, 'career.html')