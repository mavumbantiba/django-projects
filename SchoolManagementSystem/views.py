from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students-list.html', {'students': students})