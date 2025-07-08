# URL 패턴을 정의하기 위한 Django 함수 import
from django.urls import path

# habit 앱에서 사용할 뷰 클래스들 import
from .views import (
    HabitListView,     # 습관 목록 보기
    HabitCreateView,   # 습관 추가
    HabitDeleteView,   # 습관 삭제
    HabitToggleView    # 습관 완료 상태 토글
)

# URL 네임스페이스 설정 (템플릿이나 reverse에서 'habit:habit_list' 형태로 사용 가능)
app_name = 'habit'

# 기능에 대한 URL 경로 
urlpatterns = [
    #  목록 페이지
    path('', HabitListView.as_view(), name='habit_list'),

    # 추가 페이지
    path('add/', HabitCreateView.as_view(), name='add'),

    # 삭제 처리
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='delete'),

    #완료 상태 토글 (완료 ↔ 미완료)
    path('toggle/<int:pk>/', HabitToggleView.as_view(), name='toggle'),
]
