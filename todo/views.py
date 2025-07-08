from django.views.generic import ListView, UpdateView, DeleteView, View 
# 리스트, 수정, 삭제, 일반 View 기능을 위한 Django 제네릭 뷰 import
from django.shortcuts import redirect
# 페이지 리다이렉트를 위한 헬퍼 함수
from django.contrib.auth.mixins import LoginRequiredMixin
# 로그인된 사용자만 접근 가능하게 만드는 믹스인
from django.urls import reverse_lazy

from .models import Task
# 할 일(Task) 모델 import

class TaskListView(LoginRequiredMixin, ListView): # 로그인한 사용자만 접근 가능한 할 일 목록 보기 클래스형 뷰
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

    def get_queryset(self):   # 사용자 본인의 할 일만 필터링해서 최신순으로 정렬
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(user=request.user, title=task_text)  
        return redirect('todo:task_list') # 목록 페이지로 리다이렉트

class TaskUpdateView(LoginRequiredMixin, UpdateView): # 로그인한 사용자만 접근 가능한 할 일 수정 뷰
    model = Task  # 수정할 대상 모델
    fields = ['title', 'description', 'due_date']  # 수정할 수 있는 필드
    template_name = 'todo/task_form.html'  # 폼 템플릿 경로
    success_url = reverse_lazy('todo:task_list')  # 수정 후 이동할 URL

# 로그인한 사용자만 접근 가능한 할 일 삭제 뷰
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task  
    template_name = 'todo/task_confirm_delete.html'  # 삭제 확인 템플릿
    success_url = reverse_lazy('todo:task_list')  # 삭제 후 이동할 URL

class TaskToggleCompleteView(LoginRequiredMixin, View): # 완료 상태를 토글(변경)하는 뷰
    def post(self, request, pk, *args, **kwargs):   # POST 요청으로 완료 상태 변경
        task = Task.objects.get(pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect('todo:task_list')   # 다시 목록으로 리다이렉트




#------------------------------------------------------------#

# TaskListView
#로그인한 사용자의 할 일 목록& POST 요청으로 새 할 일을 생성
#리스트와 폼 처리를 동시에 담당하는 뷰

#TaskUpdateView
#선택한 할 일(Task)의 제목, 설명, 마감일을 수정하는 뷰
#수정 완료 후 목록 페이지로 리다이렉트

#TaskDeleteView
#사용자가 특정 할 일을 삭제할 수 있도록 확인 
#삭제 후 목록 페이지로 이동

#TaskToggleCompleteView
#완료 여부를 토글(체크/해제)하는 기능을 POST 요청으로  처리시킴
#상태 변경 후 다시 목록 페이지로 리다이렉트
#------------------------------------------------------------#