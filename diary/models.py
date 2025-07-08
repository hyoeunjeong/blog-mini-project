from django.db import models
from django.conf import settings
from django.utils import timezone

class Diary(models.Model):
    EMOTION_CHOICES = [
        ('😁', '행복'),
        ('😐', '보통'),
        ('😞', '슬픔'),
        ('😭', '눈물'),
    ]

    content = models.TextField()
    emotion = models.CharField(max_length=2, choices=EMOTION_CHOICES)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name = '일기'
        verbose_name_plural = '일기들'
        unique_together = ('user', 'date')  
    def __str__(self):
        return f"{self.date} - {self.emotion} - {self.user.username}"
