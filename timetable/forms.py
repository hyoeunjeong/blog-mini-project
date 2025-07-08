# Django의 폼 기능 import
from django import forms
# Timetable 모델 import
from .models import Timetable


# ModelForm 클래스 정의
class TimetableForm(forms.ModelForm):

    # Meta 클래스
        model = Timetable  # 연결할 모델은 Timetable

        # 사용자에게 입력받을 필드 목록 
        fields = [
            'subject',      # 과목명
            'professor',    # 교수명 
            'location',     # 강의실 
            'weekday',      # 요일
            'start_time',   # 시작 시간
            'end_time'      # 종료 시간
        ]

        # 필드에 사용할 위젯 설정 
        widgets = {
        
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

