from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 보여줄 필드 설정 (필요에 따라 수정 가능)
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),  # bio 필드가 추가된 경우
    )
