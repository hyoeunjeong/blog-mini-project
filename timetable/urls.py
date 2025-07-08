# URL 경로 설정을 위한 Django 함수 import
from django.urls import path
# 디렉토리의 views 모듈 import
from . import views

app_name = 'timetable'
# URL 패턴 정의
urlpatterns = [
    # 시간표 전체 보기 
    path('', views.timetable_view, name='view'),

    # 새 시간표 항목 추가 폼 (timetable_create 함수 실행?)
    path('add/', views.timetable_create, name='add'),

    #  수정 폼
    path('<int:pk>/edit/', views.timetable_edit, name='edit'),

    # 시간표 항목 삭제 확인 및 처리
    path('<int:pk>/delete/', views.timetable_delete, name='delete'),
]
