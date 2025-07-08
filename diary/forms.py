from django import forms
from .models import Diary

EMOTION_CHOICES = [
    ('😁', '😁 행복'),
    ('😐', '😐 보통'),
    ('😞', '😞 슬픔'),
    ('😭', '😭 눈물'),
]

class DiaryForm(forms.ModelForm):
    emotion = forms.ChoiceField(choices=EMOTION_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Diary
        fields = ['content', 'emotion']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
