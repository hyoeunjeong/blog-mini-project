# Django의 폼 기능을 사용하기 위해 import
from django import forms
# Task 모델을 import
from .models import Task
# Task 모델 기반으로 자동 생성되는 ModelForm 클래스
class TaskForm(forms.ModelForm):
    
    # Meta 내부 클래스
    class Meta:
        model = Task 
        fields = ['title', 'description', 'due_date', 'completed']
       
        #title: 할 일 제목
        #description: 설명 (선택적)
        #due_date: 마감일
        #completed: 완료 여부 체크박스
