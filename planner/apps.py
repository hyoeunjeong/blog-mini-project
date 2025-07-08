# Django 앱 구성을 위한 AppConfig 클래스 import
from django.apps import AppConfig
# 설정 클래스를 정의
class PlannerConfig(AppConfig):
    # 모델에서 기본 primary key로 사용할 필드 타입 지정 (64비트 자동 증가 정수)
    # → models에서 id 필드를 명시하지 않아도 BigAutoField가 자동으로 설정됨
    default_auto_field = 'django.db.models.BigAutoField'

    # 이 앱의 이름
    name = 'planner'
