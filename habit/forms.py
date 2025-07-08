from django import forms
# Django의 폼 기능을 사용하기 위한 import
from django import forms

# Habit 모델 import (이 모델을 기반으로 폼을 생성)
from .models import Habit


# ModelForm 클래스
class HabitForm(forms.ModelForm):

    # 내부 Meta 클래스: 어떤 모델과 어떤 필드를 사용할지 정의
    class Meta:
        model = Habit  # 연결할 모델: Habit

        # 사용자에게 입력 받을 필드 목록
        fields = ['name', 'date']  # 체크 여부는 자동 처리

        # 입력 위젯 설정 
        widgets = {
            # 습관 이름 입력 필드 (텍스트 상자 + Bootstrap 클래스 + placeholder)
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '습관 이름'
            }),

            # 날짜 입력 필드 (HTML5 날짜 선택기 + Bootstrap 클래스)
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
