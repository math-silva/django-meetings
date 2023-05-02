from django.contrib.auth.models import User
from django import forms
from .models import Meeting

CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('name', 'date', 'start_time', 'end_time', 'location', 'agenda', 'participants')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Meeting name',
                'class': CLASS
            }),
            'date': forms.DateInput(attrs={
                'placeholder': 'Meeting date',
                'id': 'datepicker',
                'class': CLASS
            }),
            'start_time': forms.TimeInput(attrs={
                'placeholder': 'Meeting start time',
                'class': CLASS
            }),
            'end_time': forms.TimeInput(attrs={
                'placeholder': 'Meeting end time',
                'class': CLASS
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Meeting location',
                'class': CLASS
            }),
            'agenda': forms.TextInput(attrs={
                'placeholder': 'Meeting agenda',
                'class': CLASS
            }), 
            'participants': forms.SelectMultiple(attrs={
                'class': CLASS
            })
        }