from django.db import models
from teachers.models import Teacher

class ClassRoom(models.Model):
    STANDARD_CHOICES = [
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    ]
    
    DIVISION_CHOICES = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    ] 
    
    standard = models.CharField(
        max_length=2,
        choices=STANDARD_CHOICES,
        null=False)
    
    division = models.CharField(
        max_length=1,
        choices=DIVISION_CHOICES,
        null=False
    )
    
    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        unique_together = ('standard' , 'division')
    
    def __str__(self):
        return f"{self.standard} - {self.division}"
    