from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    
    context = {
        'students' : students
    }
    
    return render(request, 'students/student_list.html', context)

def student_create(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        student = form.save(commit=False)
        
        user = User.objects.create_user(
            username=student.name,
            password=student.roll_no,
            role = 'student'
        )
        
        student.user = user
        
        student.save()
        return redirect('student_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'students/student_form.html', context)

def student_update(request, pk):
    student = get_object_or_404(
        Student,
        pk=pk
    )
    
    form = StudentForm(
        request.POST or None,
        request.FILES or None,
        instance=student
    )
    
    if form.is_valid():
        form.save()
        return redirect('student_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'students/student_form.html', context)

def student_delete(request, pk):
    student = get_object_or_404(
        Student,
        pk=pk
    )
    
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    
    context = {
        'student' : student
    }
    
    return render(request, 'students/student_delete.html', context)