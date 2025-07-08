# Django 모델 기능을 사용하기 위한 기본 import
from django.db import models

# 현재 사용 중인 사용자 모델(AUTH_USER_MODEL) 
from django.conf import settings


#  데이터를 저장하는 모델
class Habit(models.Model):
    # 습관을 소유한 사용자
    # 사용자가 삭제되면 그에 따른 내용 삭제
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 습관 이름 
    name = models.CharField("습관 이름", max_length=100)

    # 수행했는지 여부 체크
    is_checked = models.BooleanField("체크 여부", default=False)

    # 적용된 날짜 
    date = models.DateField("날짜")

    # 생성된 날짜 및 시간 (
    created_at = models.DateTimeField("생성일", auto_now_add=True)


    # 메타 옵션: 관리자 페이지 및 정렬 관련 설정
    class Meta:
        verbose_name = "습관"              # 단수형 이름
        verbose_name_plural = "습관 목록"  # 복수형 이름

    # 객체를 문자열로 출력할 때 표시될 형식
    def __str__(self):
        return f"{self.user.username} - {self.name}"
