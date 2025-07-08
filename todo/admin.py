# todo/admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'due_date', 'completed']
    list_filter = ['completed', 'due_date']
    search_fields = ['title', 'description']
