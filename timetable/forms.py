from django import forms
from .models import Timetable



class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable  

       
        fields = [
            'subject',      # 과목명
            'professor',    # 교수명
            'location',     # 강의실
            'weekday',      # 요일
            'start_time',   # 시작 시간
            'end_time'      # 종료 시간
        ]

       
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
