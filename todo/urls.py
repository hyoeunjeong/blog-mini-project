# todo/urls.py
from django.urls import path
from .views import TaskListView, TaskUpdateView, TaskDeleteView, TaskToggleCompleteView

app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/toggle/', TaskToggleCompleteView.as_view(), name='toggle'),
]
