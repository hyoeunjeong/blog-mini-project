from django.contrib import admin
from .models import StudyPlan  

@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'goal', 'created_at']
    search_fields = ['goal', 'user__username']
    ordering = ['-created_at']
