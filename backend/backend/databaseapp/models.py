from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Job(models.Model):

    Job_id = models.AutoField(primary_key=True)
    Job_location = models.CharField(max_length=100)
    Language_preferences = models.CharField(max_length=20, choices=(()))
    Wages_per_hour = models.IntegerField(MinValueValidator(2000))
    Contract_tenure = models.DurationField()
    required_skills = models.TextField()
    Job_status = models.BooleanField(default=False)
    Employer_contact_number = models.CharField(max_length=20, blank=False)
    Number_of_vacancies = models.PositiveIntegerField(MinValueValidator(0))


class Complaint(models.Model):

    ComplaintID = models.AutoField(primary_key=True)
    Complaint_by = models.CharField(max_length=50)
    Complaint_of = models.CharField(max_length=50, blank=False)
    Complaint_description = models.CharField(max_length=300)
    Complaint_resolution_status = models.BooleanField(default=False)