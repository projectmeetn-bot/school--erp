from django.shortcuts import render,redirect, get_object_or_404

from .models import ClassRoom
from .forms import ClassRoomForm

def classroom_list(request):
    classrooms = ClassRoom.objects.all()
    
    context = {
        'classrooms' : classrooms
    }
    return render(request, 'classes/classroom_list.html', context)

def classroom_create(request):
    form = ClassRoomForm(
        request.POST or  None
    )
    
    if form.is_valid():
        form.save()
        return redirect('classroom_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'classes/classroom_form.html', context)

def classroom_update(request, pk):
    classroom = get_object_or_404(
        ClassRoom,
        pk=pk
    )
    form = ClassRoomForm(
        request.POST or None,
        instance=classroom
    )
    
    if form.is_valid():
        form.save()
        return redirect('classroom_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'classes/classroom_form.html', context)
    
def classroom_delete(request, pk):
    classroom = get_object_or_404(
        ClassRoom,
        pk=pk
    )
    
    if request.method == "POST":
        classroom.delete()
        return redirect('classroom_list')
    
    context = {
        'classroom' : classroom
    }
    
    return render(request, 'classes/classroom_delete.html', context)