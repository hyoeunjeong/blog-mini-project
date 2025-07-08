# Django 모델 기능 사용을 위한 import
from django.db import models

# 현재 설정된 사용자 모델 (AUTH_USER_MODEL)을 참조하기 위한 import
from django.conf import settings


# ✅ Task 모델: 사용자별 할 일 데이터를 저장하는 모델
class Task(models.Model):
    # 이 할 일을 소유한 사용자 (User와 1:N 관계)
    # 사용자가 삭제되면 할 일도 함께 삭제됨 (CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 할 일 제목 최대 100자
    title = models.CharField("할 일", max_length=100)

    # 할 일 설명 (선택 사항, 공백 가능)
    description = models.TextField("설명", blank=True)

    # 마감일 (선택 사항, blank 모두 허용)
    due_date = models.DateField("마감일", blank=True)

    # 완료 여부  기본은 미완으로
    completed = models.BooleanField("완료 여부", default=False)

    # 생성일 자동으로 현재 시간 저장)
    created_at = models.DateTimeField("생성일", auto_now_add=True)

    # 모델에 대한 메타 정보 설정
    class Meta:
        # 생성일 기준으로 최신 순 정렬
        ordering = ['-created_at']
        # 관리자 페이지에서 보일 이름 (단수/복수)
        verbose_name = "할 일"
        verbose_name_plural = "할 일 목록"

    # 객체를 문자열로 표현할 때 보여줄 내용 (예: [user1] 과제 제출)
    def __str__(self):
        return f"[{self.user.username}] {self.title}"
