from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']
        
        widgets = {
            'roll_no' : forms.TextInput(attrs={'class' : 'form-control'}),
            'enrollment_no' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'mobile' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.Textarea(attrs={'class' : 'form-control' , 'rows' : 3}),
            'classroom' : forms.Select(attrs={'class' : 'form-select'}),
            'photo' : forms.FileInput(attrs={'class' : 'form-control'}),
        }