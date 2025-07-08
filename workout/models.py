from django.db import models
from django.conf import settings

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("운동명", max_length=100)
    duration = models.PositiveIntegerField("운동 시간(분)", help_text="분 단위")
    date = models.DateField("운동 날짜", auto_now_add=False)

    class Meta:
        ordering = ['-date']
        verbose_name = "운동 기록"
        verbose_name_plural = "운동 기록들"

    def __str__(self):
        return f"{self.date} - {self.name} ({self.duration}분)"
