# account/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'  # 🔒 namespace 설정

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ✅ 비밀번호 변경 뷰 (성공 시 홈으로 이동)
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change.html',
        success_url='/'  # ← 여기 홈 경로로 설정
    ), name='password_change'),
]

