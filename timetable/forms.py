from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        
        widgets = {
            'classroom' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),
            'subject' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),
            'teacher' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),   
            'day' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'start_time' : forms.TimeInput(
                attrs={'type' : 'time'}
            ),
            'end_time' : forms.TimeInput(
                attrs={'type' : 'time'}
            ),
        }