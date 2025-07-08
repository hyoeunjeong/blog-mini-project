from django.urls import path
from .views import (
    WorkoutListView,
    WorkoutCreateView,
    WorkoutUpdateView,
    WorkoutDeleteView,
)

app_name = 'workout'

urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout_list'),
    path('add/', WorkoutCreateView.as_view(), name='workout_add'),
    path('edit/<int:pk>/', WorkoutUpdateView.as_view(), name='workout_edit'),
    path('delete/<int:pk>/', WorkoutDeleteView.as_view(), name='workout_delete'),
]
