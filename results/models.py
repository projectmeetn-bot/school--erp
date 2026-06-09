from django.db import models

from students.models import Student
from subjects.models import Subject
from examinations.models import Examination

class Result(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    
    exam = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE
    )
    
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    
    marks = models.FloatField()
    
    total_marks = models.FloatField(
        default=100
    )
    
    @property
    def percentage(self):
        return (self.marks / self.total_marks) * 100
    
    @property
    def grade(self):
        p = self.percentage
        
        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        return "Fail"
    
    def __str__(self):
        return f"{self.student.name}"
    