# Django 관리자 기능을 사용하기 위한 admin 모듈 import
from django.contrib import admin

# Timetable 모델 import 
from .models import Timetable


#Timetable 모델을 관리자(admin) 페이지에 등록
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    # 목록 
   
    list_display = ('subject', 'weekday', 'start_time', 'end_time', 'professor', 'user')

 
    list_filter = ('weekday', 'user')

    
    search_fields = ('subject', 'professor', 'location')
