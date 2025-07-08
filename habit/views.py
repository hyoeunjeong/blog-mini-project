from django.views.generic import ListView, CreateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Habit

# ✅ 습관 목록 보기
class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'habit/habit_list.html'
    context_object_name = 'habits'

    def get_queryset(self):
        # 로그인한 유저의 습관만 최신순으로 보여줌
        return Habit.objects.filter(user=self.request.user).order_by('-created_at')


# ✅ 습관 추가
class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['name']  # 사용자 입력 필드
    template_name = 'habit/habit_form.html'
    success_url = reverse_lazy('habit:habit_list')

    def form_valid(self, form):
        # 현재 로그인한 사용자 정보 저장
        form.instance.user = self.request.user
        return super().form_valid(form)


# ✅ 습관 삭제
class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'habit/habit_confirm_delete.html'
    success_url = reverse_lazy('habit:habit_list')

    def get_queryset(self):
        # 본인의 습관만 삭제 가능
        return Habit.objects.filter(user=self.request.user)


# ✅ 체크 상태 토글 (예: 완료 여부 체크박스)
class HabitToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        habit = Habit.objects.get(pk=pk, user=request.user)
        habit.is_checked = not habit.is_checked
        habit.save()
        return redirect('habit:habit_list')
