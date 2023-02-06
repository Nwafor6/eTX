from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (AdmittedSession,
Semester,
Student,
SessionCompleted,
Course,
Department,
CGPA
)

# Register your models here.

admin.site.register(AdmittedSession)
admin.site.register(SessionCompleted)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(CGPA)
@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
	list_display=('course_title','course_code','credit_load','semester','student','test_score','exam_score','grade','created')

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
	list_display=('admitted_session','name','reg_number')

