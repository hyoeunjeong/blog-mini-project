# Django 앱 설정을 위한 AppConfig 클래스 import
from django.apps import AppConfig
# 클래스 정의
class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
