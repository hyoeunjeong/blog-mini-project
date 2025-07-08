# habit/forms.py
from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '습관 이름'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
