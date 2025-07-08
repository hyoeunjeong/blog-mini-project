from django.urls import path
from .views import (
    Index, Write, Update, Delete, DetailView,
    CommentWrite, CommentDelete, CommentEdit,
    HashTagWrite, HashTagDelete,
    toggle_like,
)

app_name = 'blog'

urlpatterns = [
    # 📄 게시글
    path('', Index.as_view(), name='post_list'),
    path('write/', Write.as_view(), name='write'),
    path('post/<int:pk>/', DetailView.as_view(), name='detail'),
    path('post/<int:pk>/edit/', Update.as_view(), name='edit'),
    path('post/<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('post/<int:pk>/like/', toggle_like, name='post_like'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),

    # 💬 댓글
    path('post/<int:pk>/comment/write/', CommentWrite.as_view(), name='comment_write'),
    path('comment/<int:pk>/edit/', CommentEdit.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),

    # #️⃣ 해시태그
    path('post/<int:pk>/hashtag/write/', HashTagWrite.as_view(), name='hashtag_write'),
    path('hashtag/<int:pk>/delete/', HashTagDelete.as_view(), name='hashtag_delete'),
]
