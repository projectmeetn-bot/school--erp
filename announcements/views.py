from django.shortcuts import render, redirect, get_object_or_404

from .models import Announcement
from .forms import AnnouncementForm


def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    
    context = {
        'announcements' : announcements
    }
    
    return render(request, 'announcements/announcement_list.html', context)

def announcement_add(request):
    form = AnnouncementForm(
        request.POST or None
    )
    
    if form.is_valid():
        form.save()
        return redirect('announcement_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'announcements/announcement_form.html', context)

def announcement_edit(request, pk):
    announcement = get_object_or_404(
        Announcement,
        pk=pk
    )
    
    form = AnnouncementForm(
        request.POST or None,
        instance=announcement
    )
    
    if form.is_valid():
        form.save()
        return redirect('announcement_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'announcements/announcement_form.html', context)        

def announcement_delete(request, pk):
    announcement = get_object_or_404(
        Announcement,
        pk=pk
    )
    
    if request.method == "POST":
        announcement.delete()
        return redirect('announcement_list')
    
    context = {
        'announcement' : announcement
    }
    
    return render(request, 'announcements/announcement_delete.html', context) 
        