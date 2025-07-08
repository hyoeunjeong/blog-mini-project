from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from account.forms import CustomUserCreationForm

# 관련 모델 import
from planner.models import PlannerTask
from todo.models import Task
from diary.models import Diary
from workout.models import Workout
from timetable.models import Timetable
from habit.models import Habit

# 홈 화면
def home(request):
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

# 회원가입
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username}님 가입을 환영합니다!")
            return redirect('login')
        else:
            messages.error(request, "회원가입에 실패했습니다. 입력 내용을 확인해주세요.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# 로그인
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{user.username}님 환영합니다.")
            return redirect('home')
        else:
            messages.error(request, "로그인 정보가 올바르지 않습니다.")
    return render(request, "registration/login.html")

# 로그아웃
def logout_view(request):
    logout(request)
    messages.success(request, "로그아웃 되었습니다.")
    return redirect('home')
