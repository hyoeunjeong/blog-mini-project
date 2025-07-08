from django.urls import path
from .views import (
    Index, Write, Update, Delete, DetailView,
    CommentWrite, CommentDelete, CommentEdit,
    HashTagWrite, HashTagDelete,
)

app_name = 'blog'

urlpatterns = [
    # =====================
    # 📄 게시글
    # =====================
    path('', Index.as_view(), name='post_list'),                        # 게시글 목록
    path('write/', Write.as_view(), name='write'),                      # 글 작성
    path('post/<int:pk>/', DetailView.as_view(), name='detail'),       # 상세 보기
    path('post/<int:pk>/edit/', Update.as_view(), name='edit'),        # 글 수정
    path('post/<int:pk>/delete/', Delete.as_view(), name='delete'),    # 글 삭제

    # =====================
    # 💬 댓글
    # =====================
    path('post/<int:pk>/comment/write/', CommentWrite.as_view(), name='comment_write'),   # 댓글 작성
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),     # 댓글 삭제
    path('comment/<int:pk>/edit/', CommentEdit.as_view(), name='comment_edit'),           # 댓글 수정

    # =====================
    # #️⃣ 해시태그
    # =====================
    path('post/<int:pk>/hashtag/write/', HashTagWrite.as_view(), name='hashtag_write'),   # 해시태그 추가
    path('hashtag/<int:pk>/delete/', HashTagDelete.as_view(), name='hashtag_delete'),     # 해시태그 삭제
]
