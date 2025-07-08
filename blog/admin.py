from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'author')
    search_fields = ('title', 'category', 'content')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)
