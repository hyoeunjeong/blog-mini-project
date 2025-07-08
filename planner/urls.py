from django.urls import path
from .views import (
    PlannerListView,
    PlannerCreateView,
    PlannerUpdateView,
    PlannerDeleteView,
)

app_name = 'planner'

urlpatterns = [
    path('', PlannerListView.as_view(), name='list'),               
    path('add/', PlannerCreateView.as_view(), name='add'),          
    path('<int:pk>/edit/', PlannerUpdateView.as_view(), name='edit'),  
    path('<int:pk>/delete/', PlannerDeleteView.as_view(), name='delete'),  
]
