from django.contrib import admin
from admission.models import Student
# Register your models here.
#admin.site.register(Student) ///or this can also used
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','father','class_name','contact']

admin.site.register(Student,StudentAdmin)