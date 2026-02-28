"""
URL configuration for App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('login/', views.custom_login, name='login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('logout/', views.custom_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('booking/', views.booking, name='booking'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('live-location/', views.live_location, name='live_location'),
    path('safety-guide/', views.safety_guide, name='safety_guide'),
    path('self-diagnosis/', views.self_diagnosis, name='self_diagnosis'),
    path('chat/', include('chat.urls')),
    path('patientreg/',views.patientreg, name='patientreg'),
    path('doctorreg/',views.doctorreg, name='doctorreg'),
    path('patientlogin/',views.patientlogin, name='patientlogin'),
]