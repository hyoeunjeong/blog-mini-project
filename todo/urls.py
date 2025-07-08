#URL 패턴을 정의 함수 import
from django.urls import path
#사용할 뷰 클래스들 import
from .views import TaskListView, TaskUpdateView, TaskDeleteView, TaskToggleCompleteView
# 앱 이름
app_name = 'todo'

# URL 리스트
urlpatterns = [
    #할일 목록 보기 + 새 할 일 추가 
    path('', TaskListView.as_view(), name='task_list'),

    #할일 수정 폼 
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),

    #할일 삭제 확인&삭제
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),

    #POST 요청, 완료 상태 토글
    path('<int:pk>/toggle/', TaskToggleCompleteView.as_view(), name='toggle'),
]
