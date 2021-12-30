from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','publish_date']
admin.site.register(Student,StudentAdmin)
