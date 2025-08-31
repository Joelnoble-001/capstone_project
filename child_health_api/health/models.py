from django.db import models
from users.models import Caregiver
from django.contrib.auth.models import User

# Create your models here.

class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    caregiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HealthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="health_records")
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    notes = models.TextField(blank=True)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Health Record for {self.child.first_name} on {self.date_recorded}"

class Vaccination(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]

    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    date_given = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.vaccine_name} - {self.status}"
