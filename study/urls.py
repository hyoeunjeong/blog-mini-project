from .views import StudyAIView, StudyPlanDetailView, StudyPlanListView
from django.urls import path



app_name = 'study'

urlpatterns = [
    path('ai-plan/', StudyAIView.as_view(), name='ai_plan'),
    path('ai-plan/<int:pk>/', StudyPlanDetailView.as_view(), name='ai_plan_detail'),
    path('my-plans/', StudyPlanListView.as_view(), name='ai_plan_list'),
]
