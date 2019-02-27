from .models import Tag

def index(request):
    tag = Tag.objects.all()
    return render(request, 'web/index.html', {'tag': tag})

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    tag =Tag(title=title, content=content)
    tag.save()
    return redirect(index)

def delete(request, pk):
    tag = Tag.objects.get(pk=pk)
    tag.delete()
    return redirect(index)









from django.shortcuts import render, redirect

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students':students})

def create(request):
    name = request.POST.get('name')
    title = redirect.POST.get('title')

    student = Student(name=name, title=title)
    student.save()
    
    return redirect('/students/')

def delete(redirect, pk):
    student = student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')