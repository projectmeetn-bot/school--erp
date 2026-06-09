from django.db import models
from teachers.models import Teacher

class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
        )
    
    code = models.CharField(
        max_length=9,
        unique=True
    )
    
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.name} ({self.code})"