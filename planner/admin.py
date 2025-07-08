from django.contrib import admin
from .models import PlannerTask

@admin.register(PlannerTask)
class PlannerTaskAdmin(admin.ModelAdmin):
    list_display = ('subject', 'exam_date', 'is_done', 'user')
    list_filter = ('is_done', 'exam_date')
    search_fields = ('subject', 'content', 'user__username')
    ordering = ('-exam_date',)
    readonly_fields = ('created_at',)
