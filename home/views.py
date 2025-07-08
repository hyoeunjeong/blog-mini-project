from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from account.forms import CustomUserCreationForm
from planner.models import PlannerTask
from todo.models import Task
from diary.models import Diary
from workout.models import Workout
from timetable.models import Timetable
from habit.models import Habit



class HomeView(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            user = request.user
            context['planner_tasks'] = PlannerTask.objects.filter(user=user).order_by('exam_date')[:5]
            context['todos'] = Task.objects.filter(user=user, completed=False).order_by('created_at')[:5]
            context['diaries'] = Diary.objects.filter(user=user).order_by('-date')[:3]
            context['workouts'] = Workout.objects.filter(user=user).order_by('-date')[:3]
            context['habits'] = Habit.objects.filter(user=user).order_by('-created_at')[:3]
            context['timetables'] = Timetable.objects.filter(user=user).order_by('weekday')[:1]
        return render(request, 'home/home.html', context)


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username}님 가입을 환영합니다!")
            return redirect('login')
        messages.error(request, "회원가입에 실패했습니다.")
        return render(request, 'registration/register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, f"{form.get_user().username}님 환영합니다.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "로그인 정보가 올바르지 않습니다.")
        return super().form_invalid(form)



class CustomLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "로그아웃 되었습니다.")
        return super().dispatch(request, *args, **kwargs)
