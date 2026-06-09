from django.db import models
from django.core.exceptions import ValidationError

from classes.models import ClassRoom
from subjects.models import Subject
from teachers.models import Teacher

class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday' , 'Monday'),
        ('Tuesday' , 'Tuesday'),
        ('Wednesday' , 'Wednesday'),
        ('Thursday' , 'Thursday'),
        ('Friday' , 'Friday'),
        ('Saturday' , 'Saturday'),
    ]
    
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )
    
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    
    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )
    
    start_time = models.TimeField()
    
    end_time = models.TimeField()
    
    def clean(self):
        teacher_exists = Timetable.objects.filter(
            teacher = self.teacher,
            day = self.day,
            start_time = self.start_time
        ).exclude(pk=self.pk)
        
        if teacher_exists.exists():
            raise ValidationError(
                "Teacher already assign"
            )
        
        classroom_exists = Timetable.objects.filter(
            classroom = self.classroom,
            day = self.day,
            start_time = self.start_time
        ).exclude(pk=self.pk)
        
        if classroom_exists.exists():
            raise ValidationError(
                "Classroom already occupied"
            )
            
            
        class Meta:
            ordering = ['day' , 'start_time']
        def __str__(self):
            return f"{self.classroom} - {self.day} - {self.subject}"
        