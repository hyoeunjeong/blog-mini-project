#Django의 모델 기능을 사용하기 위한 import
from django.db import models
#사용자 모델 설정을 참조하기 위한 import
from django.conf import settings
#기본 날짜 설정을 위한 timezone 모듈
from django.utils import timezone
# ✅ 사용자별 감정과 내용을 포함한 일기 모델
class Diary(models.Model):

    # 감정 선택지 (이모지와 한글 감정 라벨)
    EMOTION_CHOICES = [
        ('😁', '행복'),
        ('😐', '보통'),
        ('😞', '슬픔'),
        ('😭', '눈물'),
    ]

    # 일기 내용 999자 까지 가능)
    content = models.TextField(max_length=999)

    # 선택된 이모지 값 저장
    emotion = models.CharField(max_length=2, choices=EMOTION_CHOICES)
    # 작성 날짜 
    date = models.DateField(default=timezone.now)
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 모델 메타 정보 
    class Meta:
        #날짜 기준 내림차순 정렬
        ordering = ['-date']

        # 관리자 페이지에서 표시될 이름
        verbose_name = '일기'
        verbose_name_plural = '일기들'

        #하루에 하나의 일기만
        unique_together = ('user', 'date')

    # 객체를 문자열로 표현할 때 사용할 형식
    def __str__(self):
    
        return f"{self.date} - {self.emotion} - {self.user.username}"
