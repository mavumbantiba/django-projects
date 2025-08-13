from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):      
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date_of_birth',)
    ordering = ('last_name', 'first_name')
