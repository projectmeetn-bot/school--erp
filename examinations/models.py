from django.db import models
from datetime import datetime

from students.models import Student
from classes.models import ClassRoom

class Examination(models.Model):
    EXAM_TYPE = [
        ('Mid Term' , 'Mid Term'),
        ('Final Exam' , 'Final Exam')
    ]
    
    exam_name = models.CharField(max_length=100)
    
    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPE
    )
    
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )
    
    start_date = models.DateField()
    
    end_date = models.DateField()
    
    form_last_date = models.DateField()
    
    is_active = models.BooleanField(
        default=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f"{self.exam_name} - {self.classroom}"
    
    
class ExamApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending' , 'Pending'),
        ('Approved' , 'Approved'),
        ('Rejected' , 'Rejected'),
    ]
    
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    
    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE
    )
    
    attendance_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    remarks = models.TextField(
        blank=True,
        null=True
    )   
    applied_at = models.DateTimeField(
        auto_now_add=True
    ) 
    
    class Meta:
        unique_together = (
            'student',
            'examination'
        )
        
    def __str__(self):
        return (
            f"{self.student.name} -"
            f"{self.examination}"
        )

class HallTicket(models.Model):
    application = models.OneToOneField(
        ExamApplication,
        on_delete=models.CASCADE
    )
    
    hall_ticket_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )
    issue_date = models.DateTimeField(
        auto_now_add=True
    )
    
    def save(self, *args, **kwargs):
        if not self.hall_ticket_number:
            last_ticket = HallTicket.objects.order_by(
                '-id'
            ).first()
            if last_ticket:
                last_number = int(
                    last_ticket.hall_ticket_number[-4:]
                )
                new_number = last_number + 1
            else:
                new_number = 1
                
            year = datetime.now().year
            
            self.hall_ticket_number = (
                f"155{year}{new_number:04d}"
            )
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.hall_ticket_number
        