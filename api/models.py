from django.db import models

# Create your models here.

class Faculty(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Conference(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE ,related_name="conference_faculty")
    paper_title = models.CharField(max_length=255)
    conference_title = models.CharField(max_length=255)
    event_date = models.DateField(auto_now_add=True)
    organised_by = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices = [('National', 'National'), ('International', 'International')])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.conference_title

class Journal(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE ,related_name="journal_faculty")
    paper_title = models.CharField(max_length=255)
    journal_title = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    entered_date = models.DateField(auto_now_add=True)
    impact_factor = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journal_title
