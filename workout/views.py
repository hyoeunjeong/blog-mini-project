# Django에서 자주 사용하는 헬퍼 함수들을 import   
from django.shortcuts import render, get_object_or_404, redirect
# 클래스 기반 뷰를 위해 필요한 제네릭 뷰들을 import
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# 로그인한 사용자만 접근 가능하게 만들어주는 믹스인
from django.contrib.auth.mixins import LoginRequiredMixin
# URL 리다이렉트 시 사용할 함수
from django.urls import reverse_lazy
# Workout 모델과 폼 import
from .models import Workout
from .forms import WorkoutForm

 #로그인한 사용자만 접근 가능 + 운동 목록을 보여주는 클래스 기반 뷰
class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = 'workouts'
    template_name = 'workout/workout_list.html'   # 사용할 템플릿 경로


    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user).order_by('-date')


#운동 추가하기
class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'  # 사용할 템플릿 경로

    success_url = reverse_lazy('workout:workout_list')  # 성공 시 리디렉션 경로

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   # 부모 클래스 메서드 호출


#운동 수정하기
class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'   # 사용할 템플릿 경로
    success_url = reverse_lazy('workout:workout_list')   # 수정 후 이동할 URL


#운동 삭제
class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'workout/workout_confirm_delete.html'  # 삭제 확인 템플릿
    success_url = reverse_lazy('workout:workout_list')   # 삭제 성공 후 이동할 URL
