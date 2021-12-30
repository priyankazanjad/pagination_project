from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator

def studentview(request):
    student = Student.objects.all()
    paginator = Paginator(student,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'StudyApp/home.html',{'page_obj':page_obj})
