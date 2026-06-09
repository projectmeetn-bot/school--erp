from django import forms
from .models import ClassRoom

class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        
        widgets = {
            'standard' : forms.Select(attrs={'class' : 'form-select'}),
            'division' : forms.Select(attrs={'class' : 'form-select'}),
            'class_teacher' : forms.Select(attrs={'class' : 'form-select'}),
        }