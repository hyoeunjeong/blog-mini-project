from django.urls import path   # Django의 path 함수를 import 
from .views import (    #views.py에서 정의한 클래스형 뷰들을 import
    WorkoutListView,    #운동 목록 보기
    WorkoutCreateView,  #운동 추가
    WorkoutUpdateView,  #운동 수정
    WorkoutDeleteView,  #운동 삭제
)

app_name = 'workout'
# URL 패턴 목록
urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout_list'),
    path('add/', WorkoutCreateView.as_view(), name='workout_add'),
    path('edit/<int:pk>/', WorkoutUpdateView.as_view(), name='workout_edit'),
    path('delete/<int:pk>/', WorkoutDeleteView.as_view(), name='workout_delete'),
]
