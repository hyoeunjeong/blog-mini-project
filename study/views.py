from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StudyPlan, StudyDayPlan
from .forms import StudyPlanForm
from django.conf import settings
from openai import OpenAI
import re

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class StudyAIView(LoginRequiredMixin, View):
    def get(self, request):
        form = StudyPlanForm()
        return render(request, 'study/study_form.html', {'form': form})

    def post(self, request):
        form = StudyPlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user

            # 🔹 상세 프롬프트
            prompt = f"""
나는 공대생 대학생이고, 회로이론 교재의 1장 내용을 공부하고 싶어.
'{plan.duration}'일 동안 1장을 공부할 수 있는 상세한 계획을 세워줘.

📌 조건:
1. 전체 흐름은 기초 개념 → 계산 적용 → 실전 예제 순서로 구성
2. 각 날짜는 3~5줄 이상으로 상세하게 설명
3. 각 Day에는 다음을 포함:
   - 공부할 소주제 (예: 전류 정의, 옴의 법칙 이해, 전력 계산 등)
   - 추천 학습 방법 (ex. 강의, 필기, 그림 그리기, 문제 풀이 등)
   - 실습 또는 계산 문제 활동 (직접 해볼 수 있는 것)
   - 복습 또는 요약 정리 팁
4. 초보 공대생도 이해할 수 있도록 쉽게 풀어줘

형식:
- 날짜 앞에 'Day N:'을 붙여줘
- 순수 텍스트로, 마크다운이나 특수기호는 쓰지 말 것
"""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            result_text = response.choices[0].message.content

            plan.result_text = result_text
            plan.save()

            self.parse_and_save_days(plan, result_text)

            return redirect('study:ai_plan_detail', pk=plan.pk)

        return render(request, 'study/study_form.html', {'form': form})

    def parse_and_save_days(self, plan, text):
        lines = text.split('\n')
        day_pattern = re.compile(r'^Day\s*(\d+):\s*(.*)')

        current_day = None
        current_content = []

        for line in lines:
            match = day_pattern.match(line)
            if match:
                if current_day:
                    StudyDayPlan.objects.create(
                        study_plan=plan,
                        day=current_day,
                        content='\n'.join(current_content).strip()
                    )
                current_day = int(match.group(1))
                current_content = [match.group(2)]
            elif current_day:
                current_content.append(line)

        if current_day:
            StudyDayPlan.objects.create(
                study_plan=plan,
                day=current_day,
                content='\n'.join(current_content).strip()
            )


class StudyPlanDetailView(LoginRequiredMixin, DetailView):
    model = StudyPlan
    template_name = 'study/study_detail.html'
    context_object_name = 'plan'


class StudyPlanListView(LoginRequiredMixin, ListView):
    model = StudyPlan
    template_name = 'study/study_list.html'
    context_object_name = 'plans'

    def get_queryset(self):
        return StudyPlan.objects.filter(user=self.request.user).order_by('-id')
