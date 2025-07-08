# Django 모델 기능을 사용하기 위한 import
from django.db import models

# 현재 프로젝트에서 사용하는 사용자 모델을 참조하기 위한 import
from django.conf import settings

# 현재 시간 관련 도구 
from django.utils import timezone


#시험 준비 계획을 저장하는 모델
class PlannerTask(models.Model):
    # 과제를 작성한 사용자와 연결 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 시험 과목명
    subject = models.CharField("시험 과목", max_length=100)

    # 공부할 내용이나 메모 
    content = models.TextField("공부 내용", blank=True)

    # 시험 날짜
    exam_date = models.DateField("시험 날짜")

    # 과제 완료 여부 체크
    is_done = models.BooleanField("완료 여부", default=False)

    # 과제 생성일
    created_at = models.DateTimeField("생성일", auto_now_add=True)


    # 메타 정보 정의 (정렬 및 관리자 표시 )
    class Meta:
        # 기본 정렬: 시험 날짜 기준 오름차순
        ordering = ['exam_date']

        # 관리자 페이지에서 표시
        verbose_name = "플래너 과제"
        verbose_name_plural = "플래너 과제들"

    # 객체를 문자열로 표현할 때 보여줄 포맷
    def __str__(self):
        
        return f"[{self.user.username}] {self.subject} - {self.exam_date}"
