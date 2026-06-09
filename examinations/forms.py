from django import forms
from .models import Examination,ExamApplication

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = [
            'exam_name',
            'exam_type',
            'classroom',
            'start_date',
            'end_date',
            'form_last_date',
            'is_active',
        ]
        widgets = {
            'exam_name' : forms.TextInput(attrs={'class':'form-control'}),
            'exam_type' : forms.Select(attrs={'class':'form-select'}),
            'classroom' : forms.Select(attrs={'class':'form-select'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control' , 'type' : 'date'}),
            'end_date' : forms.DateInput(attrs={'class':'form-control' , 'type' : 'date'}),
            'form_last_date' : forms.DateInput(attrs={'class':'form-control' , 'type' : 'date'}),
            'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
        
class ExamApplicationForm(forms.ModelForm):
    class Meta:
        model = ExamApplication
        fields = []