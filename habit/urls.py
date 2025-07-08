from django.urls import path
from .views import (
    HabitListView,
    HabitCreateView,
    HabitDeleteView,
    HabitToggleView
)

app_name = 'habit'

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),  
    path('add/', HabitCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='delete'),
    path('toggle/<int:pk>/', HabitToggleView.as_view(), name='toggle'),
]
