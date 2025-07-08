from django.apps import AppConfig

# Workout 앱의 설정 클래스 정의
class WorkoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #데이터 과부화 방지>
    name = 'workout'     # 앱의 실제 Python 경로
