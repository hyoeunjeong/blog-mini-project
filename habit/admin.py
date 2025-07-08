from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_checked', 'user')
    list_filter = ('date', 'is_checked')
    search_fields = ('name', 'user__username')
    ordering = ('-date',)
    readonly_fields = ('user',)
