from django.contrib import admin
from django_orm.models import Student

# Register your models here.

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #pass
    list_display = ['stuName', 'stuAge', 'stuEmail', 'stuMarks']
    list_editable = ['stuMarks']
    
admin.site.register(Student, StudentAdmin)