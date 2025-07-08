# Django 앱 구성을 위한 AppConfig 클래스 import
from django.apps import AppConfig


# 앱의 설정 클래스를 정의
class HabitConfig(AppConfig):
    # 모델에서 기본으로 사용할 기본키 타입 설정
    default_auto_field = 'django.db.models.BigAutoField'

    # 이 앱의 이름
    name = 'habit'
