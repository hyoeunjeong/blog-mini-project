from django import forms
from .models import StudyPlan

class StudyPlanForm(forms.ModelForm):
    class Meta:
        model = StudyPlan
        fields = ['subject', 'goal', 'duration']
        labels = {
            'subject': '공부 주제',
            'goal': '공부 목표',
            'duration': '기간 (일)',
        }
        widgets = {
            'subject': forms.TextInput(attrs={
                'placeholder': '예: 영어, 수학'
            }),
            'goal': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': '예: 단어 암기, 문제 풀이'
            }),
            'duration': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': '예: 7'
            }),
        }
