from django.contrib import admin
from .models import Timetable

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'weekday', 'start_time', 'end_time', 'professor', 'user')
    list_filter = ('weekday', 'user')
    search_fields = ('subject', 'professor', 'location')

