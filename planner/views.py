# Django에서 제공하는 제네릭 뷰 import 목록/ 생성/수정/삭제
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# URL 리다이렉트 시 사용되는 lazy 함수
from django.urls import reverse_lazy

# 로그인한 사용자만 접근 가능하게 해주는 믹스인
from django.contrib.auth.mixins import LoginRequiredMixin

# PlannerTask 모델 import
from .models import PlannerTask

# 날짜 계산용 표준 모듈
from datetime import date, timedelta


# 학습 계획 목록
class PlannerListView(LoginRequiredMixin, ListView):
    model = PlannerTask  # 연결된 모델
    context_object_name = 'tasks'  # 템플릿에서 사용할 변수 이름
    template_name = 'planner/planner_list.html'  # 사용할 템플릿 

    # 현재 로그인한 사용자에 해당하는 데이터만 필터링
    def get_queryset(self):
        return PlannerTask.objects.filter(user=self.request.user)

    # 추가적인 컨텍스트 데이터 전달: 진행률
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks']
        total = tasks.count()  # 전체 계획 수
        done = tasks.filter(is_done=True).count()  # 완료된 계획 수
        context['progress'] = int((done / total) * 100) if total > 0 else 0  # 완료 퍼센트
        context['today_plus_2'] = date.today() + timedelta(days=2)  
        return context


#학습 계획 생성 
class PlannerCreateView(LoginRequiredMixin, CreateView):
    model = PlannerTask
    fields = ['subject', 'content', 'exam_date', 'is_done']  # 입력 
    template_name = 'planner/planner_form.html'  # 폼 템플릿
    success_url = reverse_lazy('planner:list')  # 저장 후 이동할 URL

    # 폼이 유효하면 현재 로그인한 사용자를 설정
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#학습 계획 수정 
class PlannerUpdateView(LoginRequiredMixin, UpdateView):
    model = PlannerTask
    fields = ['subject', 'content', 'exam_date', 'is_done']  # 수정 가능
    template_name = 'planner/planner_form.html'  # 폼 템플릿
    success_url = reverse_lazy('planner:list')  # 수정 후 이동


# 학습 계획 삭제 
class PlannerDeleteView(LoginRequiredMixin, DeleteView):
    model = PlannerTask
    template_name = 'planner/planner_confirm_delete.html'  # 삭제 확인 템플릿
    success_url = reverse_lazy('planner:list')  # 삭제 후 목록으로 이동
