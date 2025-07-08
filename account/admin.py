from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# User 모델을 Django 관리자에 등록
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),  
    )
