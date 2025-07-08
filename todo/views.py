# todo/views.py
from django.views.generic import ListView, UpdateView, DeleteView, View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(user=request.user, title=task_text)  # ✅ 필드명 수정
        return redirect('todo:task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

class TaskToggleCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        task = Task.objects.get(pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect('todo:task_list')
