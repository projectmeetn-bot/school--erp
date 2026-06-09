from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Attendance, AttendanceDetail
from students.models import Student
from classes.models import ClassRoom

def take_attendance(request):
    if request.method == "POST":
        
        classroom_id = request.POST.get('classroom')
        attendance_date = request.POST.get('date')
        
        classroom = get_object_or_404(
            ClassRoom,
            id=classroom_id
        )
        
        attendance, created = Attendance.objects.get_or_create(
            classroom=classroom,
            date=attendance_date
        )
        
        students = Student.objects.filter(
            classroom=classroom
        )
        
        for student in students:
            
            status = request.POST.get(
                f"student_{student.id}"
            )
            
            AttendanceDetail.objects.update_or_create(
                attendance=attendance,
                student=student,
                defaults={
                    'status' : status
                }
            )
        return redirect('attendance_list')
    classrooms = ClassRoom.objects.all()
    
    context = {
        'classrooms' : classrooms
    }
    return render(request, 'attendance/take_attendance.html', context)

def get_students(request):
    classroom_id = request.GET.get('classroom')
    
    students = Student.objects.filter(
        classroom_id=classroom_id
    )
    
    data = []
    
    for student in students:
        data.append({
            'id' : student.id,
            'name' : student.name,
            'roll_no' : student.roll_no,
            'enrollment_no' : student.enrollment_no,
        })
    return JsonResponse(data, safe=False)

def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date')
    
    context = {
        'attendances' : attendances
    }
    return render(request, 'attendance/attendance_list.html', context)

def attendance_detail(request, pk):
    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )
    
    details = AttendanceDetail.objects.filter(
        attendance=attendance
    )
    
    context = {
        'attendance' : attendance,
        'details' : details
    }
    
    return render(request, 'attendance/attendance_detail.html', context)

def delete_attendance(request, pk):
    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )
    
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')
    
    context = {
        'attendance' : attendance
    }
    
    return render(request, 'attendance/delete_attendance.html', context)
    
    