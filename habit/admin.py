# Django의 관리자(admin) 기능을 사용하기 위한 모듈 import
from django.contrib import admin

# habit 앱의 Habit 모델 import
from .models import Habit


# Django 관리자 페이지에 등록
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):

    # 목록 페이지
    
    list_display = ('name', 'date', 'is_checked', 'user')

    # 필터 사이드바
    # 날짜별 또는 체크 여부별로 필터링
    list_filter = ('date', 'is_checked')

    #  검색창에서 검색 가능
    # 습관 이름 또는 사용자 이름(username)으로 검색 가능
    search_fields = ('name', 'user__username')

    # 목록 정렬 기준 설정 
    ordering = ('-date',)

    # 관리자 폼에서 읽기 전용
    # 사용자는 'user' 필드를 수정할 수 없음
    readonly_fields = ('user',)
