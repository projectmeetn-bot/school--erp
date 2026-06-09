from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
        
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 5
                }
            ),
        }