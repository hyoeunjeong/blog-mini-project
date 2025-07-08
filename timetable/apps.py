# Django 앱 설정 기능을 제공하는 AppConfig 클래스 import
from django.apps import AppConfig

# 클래스 정의
class TimetableConfig(AppConfig):
    # 기본 기본키 필드를 64비트 자동 증가 필드(BigAutoField)로 지정
    # → models에서 id 필드를 명시하지 않아도 BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # 앱 이름 설정 
    name = 'timetable'



##AppConfig는 각 앱의 이름, 설정값, 초기화 로직 등을 Django에 알려주는 설정 클래스