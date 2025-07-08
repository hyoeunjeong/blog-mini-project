from django.contrib import admin
from .models import Diary

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'emotion', 'user')
    list_filter = ['date', 'emotion']
    search_fields = ['content', 'user__username']
    readonly_fields = ['user']
