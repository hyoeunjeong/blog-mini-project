from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Workout
from .forms import WorkoutForm

# 🏋️ 운동 목록
class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = 'workouts'
    template_name = 'workout/workout_list.html'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user).order_by('-date')


# ➕ 운동 추가
class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'
    success_url = reverse_lazy('workout:workout_list')  # ✅ 수정

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ✏️ 운동 수정
class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout/workout_form.html'
    success_url = reverse_lazy('workout:workout_list')  # ✅ 수정


# 🗑 운동 삭제
class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'workout/workout_confirm_delete.html'
    success_url = reverse_lazy('workout:workout_list')  # ✅ 수정
