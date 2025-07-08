from django.urls import path
from .views import StudyAIView, StudyPlanDetailView, StudyPlanListView

app_name = 'study'

urlpatterns = [
    # AI 공부 계획 생성 
    path('create/', StudyAIView.as_view(), name='plan_create'),
    
    # 
    path('ai-plan/', StudyAIView.as_view(), name='ai_plan'),  

    # 특정 계획 상세 보기
    path('<int:pk>/', StudyPlanDetailView.as_view(), name='plan_detail'),

    # 나의 모든 계획 목록
    path('my/', StudyPlanListView.as_view(), name='plan_list'),
]
