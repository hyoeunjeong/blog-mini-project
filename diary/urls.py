from django.urls import path
from .views import (
    DiaryListView,
    DiaryDetailView,
    DiaryWriteView,
    DiaryUpdateView,
    DiaryDeleteView,
)

app_name = 'diary'

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('write/', DiaryWriteView.as_view(), name='write'),
    path('<int:pk>/', DiaryDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', DiaryUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
]
