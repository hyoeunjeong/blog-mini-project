# Django의 URL 패턴을 정의하기 위한 path 함수 import
from django.urls import path

# diary 앱의 뷰 클래스들 import
from .views import (
    DiaryListView,     # 일기 목록 보기
    DiaryDetailView,   # 일기 상세 보기
    DiaryWriteView,    # 일기 작성
    DiaryUpdateView,   # 일기 수정
    DiaryDeleteView,   # 일기 삭제
)


app_name = 'diary'

# URL  정의
urlpatterns = [
    # 일기 목록 보기
    path('', DiaryListView.as_view(), name='list'),

    # 새 일기 작성
    path('write/', DiaryWriteView.as_view(), name='write'),

    # 특정 일기 상세 보기 (기본키 기준)
    path('<int:pk>/', DiaryDetailView.as_view(), name='detail'),

    # 특정 일기 수정
    path('<int:pk>/edit/', DiaryUpdateView.as_view(), name='edit'),

    #특정 일기 삭제
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
]
