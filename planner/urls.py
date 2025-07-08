from django.urls import path
from .views import (
    PlannerListView,
    PlannerCreateView,
    PlannerUpdateView,
    PlannerDeleteView,
)

app_name = 'planner'

urlpatterns = [
    path('', PlannerListView.as_view(), name='list'),               # 📋 시험 계획 목록
    path('add/', PlannerCreateView.as_view(), name='add'),          # ➕ 시험 계획 추가
    path('<int:pk>/edit/', PlannerUpdateView.as_view(), name='edit'),  # ✏️ 수정
    path('<int:pk>/delete/', PlannerDeleteView.as_view(), name='delete'),  # 🗑️ 삭제
]
