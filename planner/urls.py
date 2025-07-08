# URL 패턴을 정의하는 Django의 path 함수 import
from django.urls import path

# planner 앱에서 사용할 뷰들 import
from .views import (
    PlannerListView,      # 목록 보기
    PlannerCreateView,    # 계획 추가
    PlannerUpdateView,    # 계획 수정
    PlannerDeleteView,    # 계획 삭제
)

# 앱 이름
app_name = 'planner'

# URL 패턴 정의
urlpatterns = [
    #계획 목록 페이지
    path('', PlannerListView.as_view(), name='list'),

    #계획 추가 폼
    path('add/', PlannerCreateView.as_view(), name='add'),

    #계획 수정 폼
    path('<int:pk>/edit/', PlannerUpdateView.as_view(), name='edit'),

    # 계획 삭제 확인 및 처리
    path('<int:pk>/delete/', PlannerDeleteView.as_view(), name='delete'),
]
