# Django의 관리자 기능을 사용하기 위한 admin 모듈 import
from django.contrib import admin
# planner 앱의 PlannerTask 모델 import
from .models import PlannerTask

#PlannerTask 모델을 관리자 페이지에 등록
@admin.register(PlannerTask)
class PlannerTaskAdmin(admin.ModelAdmin):

    # 목록 화면에서 표시할 필드(열) 지정
   
    list_display = ('subject', 'exam_date', 'is_done', 'user')

    #필터 기능 추가 
    list_filter = ('is_done', 'exam_date')

    #검색 가능
    search_fields = ('subject', 'content', 'user__username')

    #기본 정렬 순서 지정 
    ordering = ('-exam_date',)

    # 읽기 전용 필드 지정 
    readonly_fields = ('created_at',)
