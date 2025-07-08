# Django 모델 기능 import
from django.db import models
# 현재 프로젝트에서 사용하는 사용자 모델 설정을 참조
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

    # 과목 이름
    subject = models.CharField("과목명", max_length=100)

    # 교수 이름 
    professor = models.CharField("교수명", max_length=50, blank=True)

    # 강의실 위치 
    location = models.CharField("강의실", max_length=100, blank=True)

    # 요일 선택지에서 고름
    weekday = models.CharField("요일", max_length=3, choices=WEEKDAYS)

    # 수업시작 
    start_time = models.TimeField("시작 시간")

    # 수업종료 
    end_time = models.TimeField("종료 시간")

      
    class Meta:
        # 요일  시작 시간 순
        ordering = ['weekday', 'start_time']
    
        verbose_name = "시간표"
        verbose_name_plural = "시간표 목록"

    # 객체를 문자열로 표현할 때 보여줄 형식
    def __str__(self):
       
        return f"{self.subject} ({self.get_weekday_display()} {self.start_time}-{self.end_time})"

