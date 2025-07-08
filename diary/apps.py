# Django 앱 구성을 위한 AppConfig 클래스 import
from django.apps import AppConfig


#diary앱의 설정 클래스를 정의
class DiaryConfig(AppConfig):
   
    default_auto_field = 'django.db.models.BigAutoField'
#이 앱의 이름 
    name = 'diary'
