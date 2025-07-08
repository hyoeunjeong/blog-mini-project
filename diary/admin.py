# Django의 관리자(admin) 기능을 사용하기 위한 모듈 import
from django.contrib import admin
# diary 앱의 Diary 모델 import
from .models import Diary


#Diary 모델을 Django 관리자에 등록 
@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):

    #목록 화면
    #날짜, 감정, 사용자명을 테이블 형태로 표시
    list_display = ('date', 'emotion', 'user')

    #사이드 필터
   
    list_filter = ['date', 'emotion']

    #검색창에서 검색 
    search_fields = ['content', 'user__username']

    #읽기 전용
    
    readonly_fields = ['user']
