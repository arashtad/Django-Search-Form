from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname")

admin.site.register(Student,StudentAdmin)

