from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    
    context = {
        'teachers' : teachers
    }
    
    return render(request, 'teachers/teacher_list.html', context)

def teacher_create(request):
    form = TeacherForm(
        request.POST or None,
        request.FILES or None
    )
    
    if form.is_valid():
        teacher = form.save(commit=False)
        
        username = teacher.name
        password = teacher.teacher_id
        
        user = User.objects.create_user(
            username=username,
            password=password,
            role='teacher'
        )
        
        teacher.user = user
        teacher.save()
        
        return redirect('teacher_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'teachers/teacher_form.html', context)

def teacher_update(request, pk):
    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )
    
    form  = TeacherForm(
        request.POST or None,
        request.FILES or None,
        instance=teacher
    )
    
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'teachers/teacher_form.html', context)

def teacher_delete(request, pk):
    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )
    
    if request.method == "POST":
        
        if teacher.user:
            teacher.user.delete()
        return redirect('student_list')
    
    context = {
        'teacher' : teacher
    }
    
    return render(request, 'teachers/teacher_delete.html', context)