# workout/forms.py

from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'duration', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '운동 이름'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '운동 시간 (분)'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
