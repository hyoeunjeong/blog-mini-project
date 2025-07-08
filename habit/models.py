from django.db import models
from django.conf import settings

class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("습관 이름", max_length=100)
    is_checked = models.BooleanField("체크 여부", default=False)
    date = models.DateField("날짜")
    created_at = models.DateTimeField("생성일", auto_now_add=True)  

    class Meta:
        verbose_name = "습관"
        verbose_name_plural = "습관 목록"

    def __str__(self):
        return f"{self.user.username} - {self.name}"
