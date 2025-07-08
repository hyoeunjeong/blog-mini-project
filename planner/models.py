from django.db import models
from django.conf import settings
from django.utils import timezone

class PlannerTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField("시험 과목", max_length=100)
    content = models.TextField("공부 내용", blank=True)
    exam_date = models.DateField("시험 날짜")
    is_done = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성일", auto_now_add=True)

    class Meta:
        ordering = ['exam_date']
        verbose_name = "플래너 과제"
        verbose_name_plural = "플래너 과제들"

    def __str__(self):
        return f"[{self.user.username}] {self.subject} - {self.exam_date}"
