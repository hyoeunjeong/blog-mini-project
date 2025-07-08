from django.urls import path
from .views import (
    Index, Write, Update, Delete, DetailView,
    CommentWrite, CommentDelete, CommentEdit,
    HashTagWrite, HashTagDelete,
    ToggleLikeView,  
)


app_name = 'blog'

urlpatterns = [
    #게시글
    path('', Index.as_view(), name='post_list'),                      #글 목록
    path('write/', Write.as_view(), name='write'),                    #글 작성
    path('post/<int:pk>/', DetailView.as_view(), name='detail'),      #글 상세
    path('post/<int:pk>/edit/', Update.as_view(), name='edit'),       #글 수정
    path('post/<int:pk>/delete/', Delete.as_view(), name='delete'),   #글 삭제
    path('post/<int:pk>/like/', ToggleLikeView.as_view(), name='post_like'),  #좋아요 

    #댓글
    path('post/<int:pk>/comment/write/', CommentWrite.as_view(), name='comment_write'),  #작성
    path('comment/<int:pk>/edit/', CommentEdit.as_view(), name='comment_edit'),          #수정
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),    #삭제

    #해시태그
    path('post/<int:pk>/hashtag/write/', HashTagWrite.as_view(), name='hashtag_write'),  #추가
    path('hashtag/<int:pk>/delete/', HashTagDelete.as_view(), name='hashtag_delete'),    #삭제
]
