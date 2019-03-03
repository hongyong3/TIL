from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students: students'})

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    
    student = Student(name=name, email=email)
    student.save()
    return redirect('/students/')

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')