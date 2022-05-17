# Generated by Django 4.0.3 on 2022-05-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_with_details', models.TextField()),
                ('usn', models.CharField(max_length=255)),
                ('program', models.CharField(choices=[('UG', 'UG'), ('PG', 'PG')], max_length=255)),
                ('type_of_activity', models.CharField(choices=[('Exta-Curricular', 'Extra-Curricular'), ('Co-Curricular', 'Co-Curricular')], max_length=255)),
                ('award', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('certificate', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AwardsAndRecognistionTeachersStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255)),
                ('award_name', models.CharField(max_length=255)),
                ('awarding_organization_details', models.TextField()),
                ('date', models.DateField()),
                ('institution_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Bookchapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_author', models.CharField(max_length=255)),
                ('title_of_the_chapter_in_the_book', models.CharField(max_length=255)),
                ('name_of_book', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('name_of_the_publisher', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('ISBN_number', models.CharField(max_length=255)),
                ('section_number', models.CharField(max_length=255)),
                ('chapter_number', models.CharField(max_length=255)),
                ('page_number', models.CharField(max_length=255)),
                ('upload_document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Bos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=255)),
                ('name_of_course', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=255)),
                ('activity', models.CharField(choices=[('Entreprenuership', 'Entreprenuership'), ('Employability', 'Employability'), ('Skill Development', 'Skill Development')], max_length=255)),
                ('acadamic_year_of_introduction', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'BOS',
            },
        ),
        migrations.CreateModel(
            name='CollabrativeActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('collabrating_agency_details', models.TextField()),
                ('student_or_faculty', models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty')], max_length=255)),
                ('participant_name', models.CharField(max_length=255)),
                ('participant_USN', models.CharField(blank=True, max_length=255, null=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('nature_of_activity', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceAttendedByTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255)),
                ('conference_name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('International', 'International'), ('National', 'National')], max_length=255)),
                ('presented_papers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceConductedInCollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(max_length=255)),
                ('date_month', models.DateField()),
                ('resource_person_details', models.TextField()),
                ('sponsored_name', models.CharField(max_length=255)),
                ('total_particpants', models.IntegerField(max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Consultants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_teacher', models.CharField(max_length=255)),
                ('name_of_department', models.CharField(max_length=255)),
                ('name_of_project', models.CharField(max_length=255)),
                ('sponsoring_agency_details', models.TextField()),
                ('date_of_receipt', models.DateField()),
                ('revenue_generated', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=255)),
                ('PAN_number', models.CharField(max_length=255)),
                ('designation', models.CharField(choices=[('Professor', 'Professor'), ('Associate professor', 'Associate professor'), ('Assistant professor', 'Assistant professor'), ('Emeritus professor', 'Emeritus professor'), ('others', 'others')], max_length=255)),
                ('date_of_birth', models.DateField()),
                ('highest_qualification', models.CharField(choices=[('PG(M-tech)', 'PG(M-tech)'), ('PhD', 'PhD')], max_length=255)),
                ('year_of_acquiring_highest_qualificatiom', models.DateField()),
                ('industry_joining_date', models.DateField(blank=True, null=True)),
                ('industry_experience', models.IntegerField(blank=True, null=True)),
                ('appointment_type', models.CharField(choices=[('Regular', 'Regular'), ('Adhoc', 'Adhoc'), ('contractual', 'contractual'), ('Full-time visiting', 'Full-time visiting')], max_length=255)),
                ('visiting_faculty', models.BooleanField()),
                ('visiting_faculty_semester', models.IntegerField(blank=True, null=True)),
                ('date_of_joining_institution', models.DateField()),
                ('job_status', models.CharField(choices=[('active', 'active'), ('leaving', 'leaving')], max_length=255)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundingStudentProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=255)),
                ('name_of_facilities', models.CharField(max_length=255)),
                ('agency_contact_details', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('name_of_consultancy', models.CharField(max_length=255)),
                ('total_amountspent', models.IntegerField()),
                ('upload_documents', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('principal_investigator', models.CharField(max_length=255)),
                ('co_principal_investigator', models.CharField(max_length=255)),
                ('funding_agency', models.CharField(max_length=255)),
                ('government_type', models.CharField(choices=[('government', 'government'), ('non government', 'non government')], max_length=255)),
                ('department_of_investigator', models.CharField(max_length=255)),
                ('sanctioned_order', models.CharField(max_length=255)),
                ('sanctioned_date', models.DateField()),
                ('funds_provied', models.CharField(max_length=255)),
                ('duration_of_project', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('author_name', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.TextField(max_length=255)),
                ('paper_title', models.CharField(max_length=255)),
                ('journal_title', models.TextField()),
                ('volume_number', models.CharField(max_length=255)),
                ('issue_number', models.CharField(max_length=255)),
                ('page_number', models.CharField(max_length=255)),
                ('publication_year', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=255)),
                ('publication_type', models.CharField(choices=[('international', 'international'), ('national', 'national')], max_length=255)),
                ('listed_in', models.CharField(choices=[('scopus', 'scopus'), ('web of science', 'web of science'), ('googles scholar', 'googles scholar')], max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ListMajorMinorResearchProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255)),
                ('project_title', models.CharField(max_length=255)),
                ('year_of_sanction', models.CharField(max_length=255)),
                ('funding_agency', models.CharField(max_length=255)),
                ('total_amount', models.CharField(max_length=255)),
                ('amount_utilzed', models.CharField(max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewCoursesIntroduced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=255)),
                ('duration_of_course', models.CharField(max_length=255)),
                ('activity', models.CharField(choices=[('Entreprenuership', 'Entreprenuership'), ('Employability', 'Employability'), ('Skill Development', 'Skill Development')], max_length=255)),
                ('year_of_introduction', models.DateField()),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDevelopmentProg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('no_of_participants_from_SIT', models.IntegerField()),
                ('number_of_participants_outside', models.IntegerField()),
                ('total_no_of_participants', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('name_of_funding_agency', models.CharField(max_length=255)),
                ('funding_agency', models.CharField(choices=[('government', 'government'), ('non_government', 'non_government')], max_length=255)),
                ('submission_date', models.DateField()),
                ('funding_amount', models.IntegerField()),
                ('duration_of_project', models.CharField(max_length=255)),
                ('name_of_pi', models.CharField(max_length=255)),
                ('name_of_co_pi', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('sanctioned', models.BooleanField()),
                ('upload_document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Seedmoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('recieved_date', models.DateField()),
                ('document_upload', models.FileField(blank=True, null=True, upload_to='')),
                ('amount_duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialLectureInCollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholar_name_with_address', models.CharField(max_length=255)),
                ('title_name', models.CharField(max_length=255)),
                ('area_of_specailization', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsHigherEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('sit_usn', models.CharField(max_length=255)),
                ('year_of_graduation', models.CharField(max_length=255)),
                ('program_graduated_from', models.CharField(max_length=255)),
                ('joined_institution_name', models.CharField(max_length=255)),
                ('admitted_programme_name', models.CharField(max_length=255)),
                ('year_of_admission', models.DateField()),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopAndSeminars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_seminar_name', models.CharField(max_length=255)),
                ('number_of_participants', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('upload_documents', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
