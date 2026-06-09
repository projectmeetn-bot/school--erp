from django import forms
from classes.models import ClassRoom

class AttendanceForm(forms.ModelForm):
    classroom = forms.ModelChoiceField(
        queryset=ClassRoom.objects.all()
    )
    
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type' : 'date'
        })
    )