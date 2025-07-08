# Django 관리자 기능 admin 모듈 import
from django.contrib import admin
# Task 모델 import 
from .models import Task


#(admin) 페이지에 등록
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # → 할 일을 등록한 사용자, 제목, 마감일, 완료 여부 표시
    list_display = ['user', 'title', 'due_date', 'completed']

    # 사이드바 필터 추가 
    list_filter = ['completed', 'due_date']

    search_fields = ['title', 'description']
