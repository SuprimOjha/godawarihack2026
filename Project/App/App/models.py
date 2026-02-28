from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    languages = models.CharField(max_length=200)  # Comma-separated: "English,Nepali,Hindi"
    rating = models.FloatField()
    rating_count = models.IntegerField()
    availability = models.CharField(max_length=20, choices=[('available','Available Today'),('week','Available This Week'),('online','Online Consultations')])
    consultation_fee = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    bio = models.TextField()
    pfp = models.URLField()  # Or use ImageField if storing images locally

    def languages_list(self):
        return self.languages.split(',')

    def __str__(self):
        return self.name
