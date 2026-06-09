from django.db import models
from accounts.models import User
from classes.models import ClassRoom

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    roll_no = models.CharField(
        max_length=6,
        unique=True
    )
    
    enrollment_no = models.CharField(
        max_length=10,
        unique=True
    )
    
    name = models.CharField(max_length=100)
    
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )
    
    email = models.EmailField(unique=True)
    
    mobile = models.CharField(max_length=10, unique=True)
    
    address = models.TextField()
    
    photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def delete(self, *args, **kwargs):
        user = self.user
        super().delete(*args, **kwargs)
        user.delete()    
        
    def __str__(self):
        return self.name