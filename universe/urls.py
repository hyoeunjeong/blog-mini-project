from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView, RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [

    path('admin/', admin.site.urls),

    #홈 & 인증
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    #블로그
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),

    #시간표
    path('timetable/', include(('timetable.urls', 'timetable'), namespace='timetable')),

    #할 일 관리
    path('todo/', include(('todo.urls', 'todo'), namespace='todo')),

    #플래너
    path('planner/', include(('planner.urls', 'planner'), namespace='planner')),

    #다이어리
    path('diary/', include(('diary.urls', 'diary'), namespace='diary')),

    #운동 기록
    path('workout/', include(('workout.urls', 'workout'), namespace='workout')),

    # 습관 체크
    path('habit/', include(('habit.urls', 'habit'), namespace='habit')),

    #AI 
    path('study/', include(('study.urls', 'study'), namespace='study')),

    #계정
    path('account/', include(('account.urls', 'account'), namespace='account')),
]

#개발 환경에서 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
