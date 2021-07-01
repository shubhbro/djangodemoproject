from django.shortcuts import render
from .forms import RegisterFrom
from django.contrib.auth.decorators import login_required
from django.contrib import messages

 
def patient(request):
    return render(request,"mysite/patient.html")

@login_required(login_url='login')  
def doctor(request):
    return render(request,"mysite/doctor.html")

def login(request):
    return render(request,'mysite/login.html')
