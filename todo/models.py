from django.db import models
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("할 일", max_length=255)
    description = models.TextField("설명", blank=True)
    due_date = models.DateField("마감일", null=True, blank=True)
    completed = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성일", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "할 일"
        verbose_name_plural = "할 일 목록"

    def __str__(self):
        return f"[{self.user.username}] {self.title}"
