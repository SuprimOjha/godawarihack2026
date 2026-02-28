from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/admin-home/')  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "registration/login.html")  

@login_required
def admin_home(request):
    return render(request, "registration/admin_home.html") 

def custom_logout(request):
    logout(request)
    return redirect('login')
 

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def booking(request):
    return render(request, 'bookAppointments.html')

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def live_location(request):
    return render(request, 'interactivemap.html')

def safety_guide(request):
    return render(request, 'safetyGuide.html')

def self_diagnosis(request):
    return render(request, 'selfDiagnosis.html')

def patientreg(request):
    return render(request,'regpatient.html')
    
def doctorreg(request):
    return render(request,'regdoctor.html') 

def patientlogin(request):
    return render(request,'patientlogin.html')