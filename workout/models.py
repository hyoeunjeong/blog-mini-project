from django.db import models # Django의 모델 기능을 사용하기 위해 import
from django.conf import settings # 사용자 모델 설정값 import

class Workout(models.Model):  #운동 기록을 저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("운동명", max_length=100)
    duration = models.PositiveIntegerField("운동 시간(분)", help_text="분 단위")
    date = models.DateField("운동 날짜", auto_now_add=False)

    class Meta: #  META : (최신 순으로 정렬)
        ordering = ['-date']
        verbose_name = "운동 기록"
        verbose_name_plural = "운동 기록들"

    def __str__(self):  # 객체를 문자열로 보여주는 형식
        return f"{self.date} - {self.name} ({self.duration}분)"
