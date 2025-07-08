# Django의 폼 기능 import
from django import forms
# Diary 모델 import
from .models import Diary


# ✅ 감정 선택지
EMOTION_CHOICES = [
    ('😁', '😁 행복'),
    ('😐', '😐 보통'),
    ('😞', '😞 슬픔'),
    ('😭', '😭 눈물'),
]
# Diary 모델 기반 폼 클래스 정의
class DiaryForm(forms.ModelForm):

    # 감정 필드를 수동으로 정의하여 select 위젯과 Bootstrap 클래스 적용
    emotion = forms.ChoiceField(
        choices=EMOTION_CHOICES,  # 선택지 지정
        widget=forms.Select(attrs={'class': 'form-select'})  # 드롭다운 스타일 지정
    )

    # 폼 설정 메타 클래스
    class Meta:
        model = Diary  # 연결
        fields = ['content', 'emotion']  #입력받을 필드

        # 필드별 입력 위젯 설정
        widgets = {
            # content 필드는 여러 줄 텍스트 입력창 + Bootstrap 클래스 + 줄 수 6줄
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
        }
