from django.shortcuts import render, redirect, get_object_or_404

from .models import Subject
from .forms import SubjectForm

def subject_list(request):
    subjects = Subject.objects.all()
    
    context = {
        'subjects' : subjects
    }
    
    return render(request, 'subjects/subject_list.html', context)


def subject_create(request):
    form = SubjectForm(
        request.POST or None
    )
    
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'subjects/subject_form.html', context)

def subject_update(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk
    )
    
    form = SubjectForm(
        request.POST or None,
        instance=subject
    )
    
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'subjects/subject_form.html', context)

def subject_delete(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk
    )
    
    if request.method == "POST":
        subject.delete()
        return redirect('subject_list')
    
    context = {
        'subject' : subject
    }
    
    return render(request, 'subjects/subject_delete.html', context)