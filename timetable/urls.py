from django.urls import path
from . import views

app_name = 'timetable'  # ✅ namespace 등록 (중요!)

urlpatterns = [
    path('', views.timetable_view, name='view'),
    path('add/', views.timetable_create, name='add'),
    path('<int:pk>/edit/', views.timetable_edit, name='edit'),
    path('<int:pk>/delete/', views.timetable_delete, name='delete'),
]
