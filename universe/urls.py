from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views

urlpatterns = [
    # 🔧 관리자 페이지
    path('admin/', admin.site.urls),

    # 🌐 홈 & 인증 관련
    path('', home_views.home, name='home'),
    path('register/', home_views.register, name='register'),
    path('login/', home_views.login_view, name='login'),
    path('logout/', home_views.logout_view, name='logout'),

    # 📝 블로그
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),

    # ⏰ 시간표 관리
    path('timetable/', include(('timetable.urls', 'timetable'), namespace='timetable')),

    # ✅ 할 일(TODO)
    path('todo/', include(('todo.urls', 'todo'), namespace='todo')),

    # 📘 시험 플래너
    path('planner/', include(('planner.urls', 'planner'), namespace='planner')),

    # 📖 다이어리
    path('diary/', include(('diary.urls', 'diary'), namespace='diary')),

    # 💪 운동 기록
    path('workout/', include(('workout.urls', 'workout'), namespace='workout')),

    # 📚 습관 체크
    path('habit/', include(('habit.urls', 'habit'), namespace='habit')),
  # AI
   path('study/', include(('study.urls', 'study'), namespace='study')),

]

# 📁 미디어 파일 서빙 (개발 환경 전용)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
