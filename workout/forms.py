from django import forms # Django의 폼 기능을 사용하기 위해 import
from .models import Workout # Workout 모델 import

class WorkoutForm(forms.ModelForm):  
    class Meta:
        model = Workout
        fields = ['name', 'duration', 'date']
         # 각 필드에 사용할 위젯 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '운동 이름'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '운동 시간 (분)'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  #날짜 선택기 사용
        }
