from django.db import models
from django.conf import settings

WEEKDAYS = [
    ('MON', '월요일'),
    ('TUE', '화요일'),
    ('WED', '수요일'),
    ('THU', '목요일'),
    ('FRI', '금요일'),
    ('SAT', '토요일'),
    ('SUN', '일요일'),
]

class Timetable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField("과목명", max_length=100)
    professor = models.CharField("교수명", max_length=50, blank=True)
    location = models.CharField("강의실", max_length=100, blank=True)
    weekday = models.CharField("요일", max_length=3, choices=WEEKDAYS)
    start_time = models.TimeField("시작 시간")
    end_time = models.TimeField("종료 시간")

    class Meta:
        ordering = ['weekday', 'start_time']
        verbose_name = "시간표"
        verbose_name_plural = "시간표 목록"

    def __str__(self):
        return f"{self.subject} ({self.get_weekday_display()} {self.start_time}-{self.end_time})"
