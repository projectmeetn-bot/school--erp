from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from .models import (
    Examination,
    ExamApplication,
    HallTicket
)

from .forms import (
    ExaminationForm,
    ExamApplicationForm
)

from students.models import Student
from attendance.models import AttendanceDetail


# ==================================
# Attendance Calculation
# ==================================

def calculate_attendance(student):

    total_days = AttendanceDetail.objects.filter(
        student=student
    ).count()

    present_days = AttendanceDetail.objects.filter(
        student=student,
        status='Present'
    ).count()

    if total_days == 0:
        return 0

    return round(
        (present_days / total_days) * 100,
        2
    )


# ==================================
# Examination List
# ==================================

def examination_list(request):

    examinations = Examination.objects.all()

    return render(
        request,
        'examinations/examination_list.html',
        {
            'examinations': examinations
        }
    )


# ==================================
# Add Examination
# ==================================

def examination_add(request):

    if request.method == 'POST':

        form = ExaminationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Examination Added Successfully'
            )

            return redirect(
                'examination_list'
            )

    else:

        form = ExaminationForm()

    return render(
        request,
        'examinations/examination_form.html',
        {
            'form': form
        }
    )


# ==================================
# Edit Examination
# ==================================

def examination_edit(request, pk):

    examination = get_object_or_404(
        Examination,
        pk=pk
    )

    if request.method == 'POST':

        form = ExaminationForm(
            request.POST,
            instance=examination
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Examination Updated Successfully'
            )

            return redirect(
                'examination_list'
            )

    else:

        form = ExaminationForm(
            instance=examination
        )

    return render(
        request,
        'examinations/examination_form.html',
        {
            'form': form
        }
    )


# ==================================
# Delete Examination
# ==================================

def examination_delete(request, pk):

    examination = get_object_or_404(
        Examination,
        pk=pk
    )

    if request.method == 'POST':

        examination.delete()

        messages.success(
            request,
            'Examination Deleted Successfully'
        )

        return redirect(
            'examination_list'
        )

    return render(
        request,
        'examinations/examination_delete.html',
        {
            'examination': examination
        }
    )


# ==================================
# Student Examination List
# ==================================

def student_examinations(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:
        messages.error(
            request,
            'Student profile not found'
        )
        return redirect('student_dashboard')

    examinations = Examination.objects.filter(
        classroom=student.classroom,
        is_active=True
    )

    return render(
        request,
        'examinations/student_examinations.html',
        {
            'examinations': examinations
        }
    )


# ==================================
# Student Apply Exam
# ==================================

def apply_exam(request, exam_id):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:
        messages.error(
            request,
            'Student profile not found'
        )
        return redirect('student_dashboard')

    examination = get_object_or_404(
        Examination,
        pk=exam_id
    )

    attendance_percentage = (
        calculate_attendance(student)
    )

    application, created = (
        ExamApplication.objects.get_or_create(
            student=student,
            examination=examination,
            defaults={
                'attendance_percentage':
                attendance_percentage
            }
        )
    )

    if created:

        messages.success(
            request,
            'Application Submitted Successfully'
        )

    else:

        messages.warning(
            request,
            'You have already applied.'
        )

    return redirect(
        'my_applications'
    )


# ==================================
# Application List
# ==================================

def application_list(request):

    applications = ExamApplication.objects.all()

    return render(
        request,
        'examinations/application_list.html',
        {
            'applications': applications
        }
    )


# ==================================
# Approve Application
# ==================================

def approve_application(request, pk):

    application = get_object_or_404(
        ExamApplication,
        pk=pk
    )

    application.status = 'Approved'
    application.save()

    HallTicket.objects.get_or_create(
        application=application
    )

    messages.success(
        request,
        'Application Approved'
    )

    return redirect(
        'application_list'
    )


# ==================================
# Reject Application
# ==================================

def reject_application(request, pk):

    application = get_object_or_404(
        ExamApplication,
        pk=pk
    )

    application.status = 'Rejected'
    application.save()

    messages.error(
        request,
        'Application Rejected'
    )

    return redirect(
        'application_list'
    )


# ==================================
# My Applications
# ==================================

def my_applications(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:
        return redirect('student_dashboard')

    applications = ExamApplication.objects.filter(
        student=student
    )

    return render(
        request,
        'examinations/my_applications.html',
        {
            'applications': applications
        }
    )


# ==================================
# Hall Ticket List
# ==================================

def hallticket_list(request):

    tickets = HallTicket.objects.all()

    return render(
        request,
        'examinations/hallticket_list.html',
        {
            'tickets': tickets
        }
    )


# ==================================
# Student Hall Tickets
# ==================================

def my_halltickets(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:
        return redirect('student_dashboard')

    tickets = HallTicket.objects.filter(
        application__student=student
    )

    return render(
        request,
        'examinations/my_halltickets.html',
        {
            'tickets': tickets
        }
    )


# ==================================
# Hall Ticket Delete
# ==================================

def hallticket_delete(request, pk):

    ticket = get_object_or_404(
        HallTicket,
        pk=pk
    )

    if request.method == 'POST':

        ticket.delete()

        messages.success(
            request,
            'Hall Ticket Deleted'
        )

        return redirect(
            'hallticket_list'
        )

    return render(
        request,
        'examinations/hallticket_delete.html',
        {
            'ticket': ticket
        }
    )


# ==================================
# Hall Ticket PDF
# ==================================

def hallticket_pdf(request, pk):

    ticket = get_object_or_404(
        HallTicket,
        pk=pk
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = f'attachment; filename="hallticket_{ticket.id}.pdf"'

    pdf = canvas.Canvas(response)

    pdf.setTitle("Hall Ticket")

    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(
        180,
        800,
        "SCHOOL ERP HALL TICKET"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        740,
        f"Hall Ticket No : {ticket.hall_ticket_number}"
    )

    pdf.drawString(
        50,
        710,
        f"Student : {ticket.application.student.name}"
    )

    pdf.drawString(
        50,
        680,
        f"Exam : {ticket.application.examination.exam_name}"
    )

    pdf.drawString(
        50,
        650,
        f"Class : {ticket.application.examination.classroom}"
    )

    pdf.drawString(
        50,
        620,
        f"Issue Date : {ticket.issue_date}"
    )

    pdf.drawString(
        50,
        560,
        "Principal Signature"
    )

    pdf.save()

    return response