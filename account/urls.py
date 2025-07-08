from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account' 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change.html',
        success_url='/'
    ), name='password_change'),


    path('profile/', views.profile_view, name='profile_view'),

    path('user/<str:username>/', views.public_profile_view, name='public_profile'),
    
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
