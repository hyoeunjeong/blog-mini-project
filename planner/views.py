from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PlannerTask
from datetime import date, timedelta


class PlannerListView(LoginRequiredMixin, ListView):
    model = PlannerTask
    context_object_name = 'tasks'
    template_name = 'planner/planner_list.html'

    def get_queryset(self):
        return PlannerTask.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks']
        total = tasks.count()
        done = tasks.filter(is_done=True).count()
        context['progress'] = int((done / total) * 100) if total > 0 else 0
        context['today_plus_2'] = date.today() + timedelta(days=2)  
        return context


class PlannerCreateView(LoginRequiredMixin, CreateView):
    model = PlannerTask
    fields = ['subject', 'content', 'exam_date', 'is_done']
    template_name = 'planner/planner_form.html'
    success_url = reverse_lazy('planner:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlannerUpdateView(LoginRequiredMixin, UpdateView):
    model = PlannerTask
    fields = ['subject', 'content', 'exam_date', 'is_done']
    template_name = 'planner/planner_form.html'
    success_url = reverse_lazy('planner:list')


class PlannerDeleteView(LoginRequiredMixin, DeleteView):
    model = PlannerTask
    template_name = 'planner/planner_confirm_delete.html'
    success_url = reverse_lazy('planner:list')
