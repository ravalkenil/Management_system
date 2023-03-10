from django.contrib import admin
from student.models import student_custom,application_model

# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','password','Role']
admin.site.register(student_custom,studentadmin)

class applicationadmin(admin.ModelAdmin):
    list_display =['application_id','university_name','program_name','study_mode','customer','status']
admin.site.register(application_model,applicationadmin)