from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user']
        
        widgets = {
            'teacher_id' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Teacher Id e.b. 23BCA001'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Teacher Full Name'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Teacher Email'}),
            'mobile' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Teacher Mobile Number'}),
            'date_of_joining' : forms.DateInput(attrs={'class' : 'form-control' , 'type' : 'date'}),
            'address' : forms.Textarea(attrs={'class' : 'form-control' , 'row' : 2}),
            'photo' : forms.FileInput(attrs={'class' : 'form-control'}),
        }