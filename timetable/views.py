from django.shortcuts import render, redirect, get_object_or_404
from datetime import time

from .models import Timetable
from .forms import TimetableForm

from classes.models import ClassRoom
from subjects.models import Subject


def timetable_list(request):
    classrooms = ClassRoom.objects.all()
    
    context = {
        'classrooms' : classrooms
    }
    
    return render(request, 'timetable/timetable_list.html', context)


def timetable_edit(request, pk):
    timetable = get_object_or_404(
        Timetable,
        pk=pk
    )
    form = TimetableForm(
        request.POST or None,
        instance=timetable
    )
    if form.is_valid():
        form.save()
        return redirect('class_timetable' , timetable.classroom.id)
    
    context = {
        'form' : form
    }
    
    return render(request, 'timetable/timetable_form.html', context)

def timetable_delete(request, pk):
    timetable = get_object_or_404(
        Timetable,
        pk=pk
    )
    classroom_id = timetable.classroom.id
    
    if request.method == "POST":
        timetable.delete()
        
        return redirect('class_timetable' , classroom_id)
    
    context = {
        'timetable' : timetable
    }
    
    return render(request, 'timetable/timetable_delete.html', context)

def generate_timetable(request, classroom_id):
    classroom = get_object_or_404(
        ClassRoom,
        id=classroom_id
    )
    subjects = list(
        Subject.objects.all()
    )
    
    if not subjects:
        return redirect('timetable_list')
    
    Timetable.objects.filter(
        classroom=classroom
        ).delete()
    
    days = [
        'Monday',
        'Tuesdady',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ]
    
    periods = [
        (time(8, 0), time(9, 0)),
        (time(9, 0), time(10, 0)),
        (time(10, 30), time(11, 30)),
        (time(11, 30), time(12, 30)),
        (time(12, 30), time(1, 0)),
    ]
    
    index = 0
    
    for day in days:
        for start, end in periods:
            subject = subjects[
                index % len(subjects)
            ]
            
            Timetable.objects.create(
                classroom=classroom,
                subject=subject,
                teacher=subject.teacher,
                day=day,
                start_time=start,
                end_time=end
            )
            index += 1
    return redirect('class_timetable', classroom_id)

def class_timetable(request, classroom_id):
    classroom = get_object_or_404(
        ClassRoom,
        id=classroom_id
    )
    
    timetable = Timetable.objects.filter(
        classroom=classroom
    ).order_by(
        'day',
        'start_time'
    )
    
    context = {
        'classroom' : classroom,
        'timetable' : timetable
    }
    
    return render(request, 'timetable/class_timetable.html', context)