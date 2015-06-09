from django.contrib import admin

from .models import Subject
from .models import Department
from .models import Faculty
from .models import Student
from .models import Tutor


class SubjectAdmin(admin.ModelAdmin):
    # list_display = ('id','name', 'kredits','semestr','group','specialization','depends_on')
    list_display = ('id','name', 'kredits','semestr','group','specialization','depends_on', 'department')
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'info','faculty')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'info')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'second_name', 'surname', 'course', 'group', 'phone_number')

class TutorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'second_name', 'surname', 'phone_number')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)


# Register your models here.
