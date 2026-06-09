from django.db import models
from accounts.models import User

class Teacher(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    teacher_id = models.CharField(
        max_length=10,
        unique=True
    )
    
    name = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    
    mobile = models.CharField(max_length=10 , unique=True)
    
    date_of_joining = models.DateField(null=True, blank=True)
    
    address = models.TextField()
    
    photo = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True
    )
    
    def delete(self, *args, **kwargs):
        user = self.user
        super().delete(*args, **kwargs)
        user.delete()
    
    def __str__(self):
        return self.name
    