from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView  # 제네릭 뷰 import
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # 로그인 및 권한 제어 믹스인
from django.urls import reverse_lazy  # 클래스 기반 뷰에서 URL 리다이렉트용
from .models import Diary  # Diary 모델 import
from .forms import DiaryForm  # DiaryForm 폼 import
from datetime import date  # 오늘 날짜 사용

# 일기 목록 보기 =로그인 시
class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    context_object_name = 'diaries'

    
    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user).order_by('-date')


#일기 
class DiaryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'
    context_object_name = 'diary'

    # 로그인한 사용자만 자기 글을 볼 수 있도록 검사
    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user


# 일기 작성 
class DiaryWriteView(LoginRequiredMixin, CreateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    # 폼이 유효할 경우 작성자와 날짜 자동 지정 후 저장
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)


# 잉기 수정 뷰 (본인만 가능)
class DiaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    # 수정 권한: 작성자 본인인지 검사
    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user


# 일기 삭제 뷰 
class DiaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diary
    template_name = 'diary/diary_confirm_delete.html'
    success_url = reverse_lazy('diary:list')

    # 삭제 -작성자 본인인지 검사
    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user
