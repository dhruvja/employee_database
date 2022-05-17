import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Bos(models.Model):
    program_name = models.CharField(max_length=255)
    name_of_course = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    activity = models.CharField(max_length=255, choices = (("Entreprenuership","Entreprenuership"),("Employability","Employability"), ("Skill Development","Skill Development")))
    acadamic_year_of_introduction = models.CharField(max_length=255)
    date = models.DateField(null=True)
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.program_name

    class Meta: verbose_name_plural = 'BOS'


class NewCoursesIntroduced(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    duration_of_course = models.CharField(max_length=255)
    activity = models.CharField(max_length=255, choices = (("Entreprenuership","Entreprenuership"),("Employability","Employability"), ("Skill Development","Skill Development")))
    year_of_introduction = models.DateField()
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name


class Consultants(models.Model):
    name_of_teacher = models.CharField(max_length=255)
    name_of_department = models.CharField(max_length=255)
    name_of_project = models.CharField(max_length=255)
    sponsoring_agency_details = models.TextField()
    date_of_receipt = models.DateField()
    revenue_generated = models.CharField(max_length=255)
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name_of_project


class Bookchapter(models.Model):
    name_of_author = models.CharField(max_length=255)
    title_of_the_chapter_in_the_book = models.CharField(max_length=255)
    name_of_book = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    name_of_the_publisher = models.CharField(max_length=255)
    year = models.IntegerField()
    ISBN_number = models.CharField(max_length=255)
    section_number = models.CharField(max_length=255)
    chapter_number = models.CharField(max_length=255)
    page_number = models.CharField(max_length=255)
    upload_document=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name_of_book


class Seedmoney(models.Model):
    faculty_name=models.CharField(max_length=255)
    amount=models.IntegerField()
    recieved_date=models.DateField()
    document_upload=models.FileField(blank=True, null=True)
    amount_duration=models.CharField(max_length=255)

    def __str__(self):
        return self.faculty_name

class Proposal(models.Model):
    amount=models.IntegerField()
    name_of_funding_agency=models.CharField(max_length=255)
    funding_agency=models.CharField(max_length=255,choices=(("government","government"),("non_government","non_government")))
    submission_date=models.DateField()
    funding_amount=models.IntegerField()
    duration_of_project=models.CharField(max_length=255)	
    name_of_pi=models.CharField(max_length=255)
    name_of_co_pi=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    sanctioned=models.BooleanField()
    upload_document=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name_of_funding_agency


class Journal(models.Model):
    author_name=models.TextField(max_length=255)
    paper_title=models.CharField(max_length=255)
    journal_title=models.TextField()
    volume_number=models.CharField(max_length=255)		
    issue_number=models.CharField(max_length=255)
    page_number=models.CharField(max_length=255)
    # month=models.DateField()
    publication_year=models.CharField(max_length=255)
    ISBN=models.CharField(max_length=255)
    publication_type=models.CharField(max_length=255,choices=(("international","international"),("national","national")))
    listed_in=models.CharField(max_length=255,choices=(("scopus","scopus"),("web of science","web of science"),("googles scholar","googles scholar")))
    document=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.journal_title


# class Awards(models.Model):
        
#     faculty_name=models.CharField(max_length=255)
#     award_name=models.CharField(max_length=255)
#     date=models.CharField(max_length=255)
#     awarding_agency=models.DateField()
#     award_type=models.CharField(max_length=255,choices=(("international","international"),("national","national")))
#     document=models.FileField(blank=True, null=True)

#     def __str__(self):
#         return self.award_name



class Grant(models.Model):
    project_name=models.CharField(max_length=255)
    principal_investigator=models.CharField(max_length=255)
    co_principal_investigator=models.CharField(max_length=255)
    funding_agency=models.CharField(max_length=255)
    government_type=models.CharField(max_length=255,choices=(("government","government"),("non government","non government")))
    department_of_investigator=models.CharField(max_length=255)
    sanctioned_order=models.CharField(max_length=255)
    sanctioned_date=models.DateField()
    funds_provied=models.CharField(max_length=255)
    duration_of_project=models.CharField(max_length=255)
    start_date=models.DateField()
    completion_date=models.DateField()
    document=models.FileField()
    author_name=models.CharField(max_length=255)
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.project_name

class WorkshopAndSeminars(models.Model):
    workshop_seminar_name=models.CharField(max_length = 255)
    number_of_participants=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    upload_documents=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.workshop_seminar_name

class FundingStudentProjects(models.Model):  
    faculty_name=models.CharField(max_length = 255)
    name_of_facilities=models.CharField(max_length = 255)
    agency_contact_details=models.IntegerField()
    issue_date=models.DateField()
    name_of_consultancy=models.CharField(max_length = 255)
    total_amountspent=models.IntegerField()
    upload_documents=models.FileField(blank=True, null=True)

    def __str__(self):
        return self.faculty_name

class CollabrativeActivity(models.Model):
    title=models.CharField(max_length = 255)
    collabrating_agency_details=models.TextField()
    student_or_faculty = models.CharField(max_length = 255, choices=(("Student", "Student"), ("Faculty", "Faculty")))
    participant_name=models.CharField(max_length = 255)
    participant_USN=models.CharField(max_length = 255, null=True, blank=True)
    from_date=models.DateField()
    to_date=models.DateField()
    nature_of_activity = models.CharField(max_length=255) # add comments
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

class Activity(models.Model):
    activity_with_details = models.TextField()
    usn = models.CharField(max_length = 255)
    program = type_of_activity = models.CharField(max_length=255,choices=(("UG","UG"),("PG","PG")))
    type_of_activity = models.CharField(max_length=255,choices=(("Exta-Curricular","Extra-Curricular"),("Co-Curricular","Co-Curricular")))
    award = models.CharField(max_length=255)
    date = models.DateField()
    certificate = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.usn


class ProfessionalDevelopmentProg(models.Model):
    title=models.CharField(max_length = 255)
    no_of_participants_from_SIT=models.IntegerField()
    number_of_participants_outside=models.IntegerField()
    total_no_of_participants=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()

    def __str__(self):
        return self.title

class ConferenceConductedInCollege(models.Model):
    conference_name=models.CharField(max_length=255)
    date_month=models.DateField()
    resource_person_details=models.TextField()
    sponsored_name=models.CharField(max_length=255)
    total_particpants=models.IntegerField(max_length=255)
    remarks=models.CharField(max_length=255, null=True, blank=True)
    document=models.FileField()

    def __str__(self):
        return self.conference_name



class ConferenceAttendedByTeachers(models.Model):
    teacher_name=models.CharField(max_length=255)
    conference_name=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    date=models.DateField()
    type=models.CharField(max_length=255,choices=(("International","International"),("National","National")))
    presented_papers_name=models.CharField(max_length=255, null=True, blank=True)
    remarks=models.CharField(max_length=255, null=True, blank=True)
    document=models.FileField()

    def __str__(self):
        return self.conference_name


class SpecialLectureInCollege(models.Model):
    scholar_name_with_address=models.CharField(max_length=255)
    title_name=models.CharField(max_length=255)
    area_of_specailization=models.CharField(max_length=255)
    date=models.DateField()
    document=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.title_name

class ListMajorMinorResearchProjects(models.Model):
    teacher_name=models.CharField(max_length=255)
    project_title=models.CharField(max_length=255)
    year_of_sanction=models.CharField(max_length=255)
    funding_agency=models.CharField(max_length=255)
    total_amount=models.CharField(max_length=255)
    amount_utilzed=models.CharField(max_length=255)
    remarks=models.CharField(max_length=255, blank=True, null=True)
    document=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.project_title


class AwardsAndRecognistionTeachersStudents(models.Model):
    activity_name=models.CharField(max_length=255)
    award_name=models.CharField(max_length=255)
    awarding_organization_details=models.TextField()
    date=models.DateField()
    institution_name=models.CharField(max_length=255)
    type=models.CharField(max_length=255,choices=(("National","National"),("International","International")))
    document=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.activity_name


class StudentsHigherEducation(models.Model):
    student_name=models.CharField(max_length=255)
    sit_usn=models.CharField(max_length=255)
    year_of_graduation=models.CharField(max_length=255)
    program_graduated_from=models.CharField(max_length=255)
    joined_institution_name=models.CharField(max_length=255)
    admitted_programme_name=models.CharField(max_length=255)
    year_of_admission=models.DateField()
    document=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.student_name

class FacultyProfile(models.Model):
    faculty_name=models.CharField(max_length=500)	
    gender=models.CharField(max_length=255,choices=(("male","male"),("female","female")))
    PAN_number=models.CharField(max_length=255)
    designation=models.CharField(max_length=255,choices=(("Professor","Professor"),("Associate professor","Associate professor"),("Assistant professor","Assistant professor"),("Emeritus professor","Emeritus professor"),("others","others")))
    date_of_birth=models.DateField()
    highest_qualification=models.CharField(max_length=255,choices=(("PG(M-tech)","PG(M-tech)"),("PhD","PhD")))
    year_of_acquiring_highest_qualificatiom=models.DateField()
    industry_joining_date=models.DateField(blank=True, null=True)
    industry_experience = models.IntegerField(null=True, blank=True)
    # regular_capacity=models.IntegerField()
    # contractual_capacity=models.IntegerField()
    # experience_in_industry=models.IntegerField()
    # total_no_of_experience=models.IntegerField()
    appointment_type=models.CharField(max_length=255,choices=(("Regular","Regular"),("Adhoc","Adhoc"),("contractual","contractual"),("Full-time visiting","Full-time visiting")))
    visiting_faculty = models.BooleanField()
    visiting_faculty_semester =models.IntegerField(blank=True, null=True)
    date_of_joining_institution=models.DateField()
    job_status=models.CharField(max_length=255,choices=(("active","active"),("leaving","leaving")))
    date_of_leaving=models.DateField(blank = True, null = True)

    def __str__(self):
        return self.faculty_name