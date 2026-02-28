from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience', 'rating', 'availability')
    search_fields = ('name', 'specialty', 'qualification', 'location')
    list_filter = ('specialty', 'availability')
