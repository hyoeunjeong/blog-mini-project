from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (  
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    ProfileEditView,
    PublicProfileView,
)

app_name = 'account'

urlpatterns = [
    #회원가입
    path('register/', RegisterView.as_view(), name='register'),
    #로그인
    path('login/', CustomLoginView.as_view(), name='login'),
    #로그아웃
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    #비밀번호 변경
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='account/password_change.html',
            success_url='/'
        ),
        name='password_change'
    ),

    #프로필 보기
    path('profile/', ProfileView.as_view(), name='profile_view'),

    #프로필 수정
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),

    #프로필 보기
    path('user/<str:username>/', PublicProfileView.as_view(), name='public_profile'),
]
