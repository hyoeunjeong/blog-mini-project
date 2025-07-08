from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Diary
from .forms import DiaryForm
from datetime import date

class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    context_object_name = 'diaries'

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user).order_by('-date')

class DiaryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'
    context_object_name = 'diary'

    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user

class DiaryWriteView(LoginRequiredMixin, CreateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)

class DiaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user

class DiaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diary
    template_name = 'diary/diary_confirm_delete.html'
    success_url = reverse_lazy('diary:list')

    def test_func(self):
        diary = self.get_object()
        return diary.user == self.request.user
