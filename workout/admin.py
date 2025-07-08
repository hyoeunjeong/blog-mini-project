from django.contrib import admin  # Django의 관리자(admin) 기능을 사용하기 위한 모듈 impor
from .models import Workout  # Workout 모델을 가져옴

@admin.register(Workout)      # 관리자 사이트에 Workout
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'date', 'user')


# 관리자 목록 페이지에서 보여줄 필드들 지정
    
    # name: 운동명
    # duration: 운동 시간(분)
    # date: 운동 날짜
    # user: 해당 운동을 등록한 사용자