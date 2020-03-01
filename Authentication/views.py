from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from Aradhya_Hospital.decorators import login_check
from django.http import QueryDict

@login_check
def signin(request):
    if request.method == 'POST':
        q_string = request.META['QUERY_STRING']
        q_dict = QueryDict(q_string)
        next = q_dict.get('next') or '/'
        try:
            username = request.POST['username']
            user = auth.authenticate(username=username,password=request.POST['password'])
            auth.login(request,user)
            return redirect(next)
        except:
            return render(request, 'Authentication/signin.html',{'message':'Username or Password is not correct'})

    return render(request, 'Authentication/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')