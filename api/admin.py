from django.contrib import admin
from .models import Bos,NewCoursesIntroduced, Consultants, Bookchapter, Seedmoney, Proposal, Journal, Grant,StudentsHigherEducation, AwardsAndRecognistionTeachersStudents, ListMajorMinorResearchProjects, SpecialLectureInCollege, ConferenceAttendedByTeachers, ConferenceConductedInCollege, ProfessionalDevelopmentProg, CollabrativeActivity, FundingStudentProjects, WorkshopAndSeminars, FacultyProfile
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
# Register your models here.

# admin.site.register(Faculty)
# admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Bookchapter)
admin.site.register(NewCoursesIntroduced)
admin.site.register(Consultants)
admin.site.register(Seedmoney)
admin.site.register(Proposal)
# admin.site.register(Awards)
admin.site.register(Grant)
admin.site.register(ConferenceConductedInCollege)
admin.site.register(SpecialLectureInCollege)
admin.site.register(ListMajorMinorResearchProjects)
admin.site.register(StudentsHigherEducation)
admin.site.register(WorkshopAndSeminars)
admin.site.register(FundingStudentProjects)
admin.site.register(CollabrativeActivity)
admin.site.register(ProfessionalDevelopmentProg)
admin.site.register(FacultyProfile)

class AwardsAndRecognistionTeachersStudentsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    # resource_class = AwardsAndRecognistionTeachersStudents
    date_hierarchy = 'date'

class BosAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    date_hierarchy = 'date'

class ConferenceAttendedByTeachersAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'conference_name')

admin.site.register(AwardsAndRecognistionTeachersStudents, AwardsAndRecognistionTeachersStudentsAdmin)
admin.site.register(Bos, BosAdmin)
admin.site.register(ConferenceAttendedByTeachers, ConferenceAttendedByTeachersAdmin)



