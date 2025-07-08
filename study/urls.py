from django.urls import path
from .views import StudyAIView, StudyPlanDetailView, StudyPlanListView

app_name = 'study'

urlpatterns = [
    # AI 공부 계획 생성 (기존: plan_create)
    path('create/', StudyAIView.as_view(), name='plan_create'),
    
    # ✅ 별칭 추가: 기존 템플릿 호환용
    path('ai-plan/', StudyAIView.as_view(), name='ai_plan'),  # ← 이 줄 추가됨!

    # 특정 계획 상세 보기
    path('<int:pk>/', StudyPlanDetailView.as_view(), name='plan_detail'),

    # 나의 모든 계획 목록
    path('my/', StudyPlanListView.as_view(), name='plan_list'),
]
