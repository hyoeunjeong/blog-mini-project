from django.db import models
from django.conf import settings

class StudyPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField("주제", max_length=100)
    goal = models.TextField("목표")
    duration = models.PositiveIntegerField("기간 (일수)")
    result_text = models.TextField("AI 생성 결과", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.user.username})"


class StudyDayPlan(models.Model):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='days')
    day = models.PositiveIntegerField("며칠째")
    content = models.TextField("계획 내용")

    def __str__(self):
        return f"Day {self.day} - {self.study_plan.subject}"
