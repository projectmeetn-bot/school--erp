from django.db import models
from students.models import Student
from classes.models import ClassRoom

class Attendance(models.Model):
    classroom = models.ForeignKey(
       ClassRoom,
       on_delete=models.CASCADE
    )
   
    date = models.DateField()
   
    created_at = models.DateTimeField(
        auto_now_add=True
    )
   
    class Meta:
       unique_together = ('classroom' , 'date')
       
    def __str__(self):
        return f"{self.classroom} - {self.date}"
    

class AttendanceDetail(models.Model):
    STATUS_CHOICES = [
        ('Present' , 'Present'),
        ('Absent' , 'Absent'),
        ('Leave' , 'Leave'),
    ]
    
    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,
        related_name='details'
    )
    
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    
    class Meta:
       unique_together = ('attendance' , 'student')
    
    def __str__(self):
        return f"{self.student.name} - {self.status}"