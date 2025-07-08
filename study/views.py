from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import StudyPlan, StudyDayPlan
from .forms import StudyPlanForm
from openai import OpenAI
import re


client = OpenAI(api_key=settings.OPENAI_API_KEY)


GPT_MODEL = "gpt-3.5-turbo"



class StudyAIView(LoginRequiredMixin, View):
    def get(self, request):
        form = StudyPlanForm()
        return render(request, 'study/study_form.html', {'form': form})

    def post(self, request):
        form = StudyPlanForm(request.POST)
        if not form.is_valid():
            return render(request, 'study/study_form.html', {'form': form})

        plan = form.save(commit=False)
        plan.user = request.user

        #  GPT 프롬프트
        prompt = f"""
나는 대학교 공대생이고 전공은 반도체와 회로야.
'{plan.subject}'라는 주제에 대해 공부할 계획이야.

다음 내용을 초보자도 이해할 수 있도록 친절하게 설명해줘:

1. 이 주제를 이해하기 위해 필요한 개념들을 기초부터 심화 순서로 정리해줘.
2. 각 개념마다 다음을 설명해줘:
   - 쉬운 설명 (전문 용어는 꼭 풀이 포함)
   - 추천 학습 방법 (강의, 필기, 그림, 문제 풀이 등)
   - 실제 예시나 비유
3. 이 주제와 관련된 대표적인 연습 문제를 최소 2개 제안해줘:
   - 난이도는 쉬운 것부터
   - 문제마다 풀이 방향이나 접근 팁도 함께 설명해줘
4. 복습이나 정리 팁도 알려줘.
5. 전체 출력은 마크다운이나 특수 기호 없이, 순수한 텍스트로 해줘.
"""

        try:
            response = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            result_text = response.choices[0].message.content.strip()
        except Exception as e:
            result_text = "ChatGPT 응답을 받는 데 문제가 발생했습니다. 다시 시도해주세요."
            print(f"[GPT 오류] {e}")

        # 저장
        plan.result_text = result_text
        plan.save()

        #  GPT 결과 Day별 파싱
        self.parse_and_save_days(plan, result_text)

        return redirect('study:plan_detail', pk=plan.pk)

    def parse_and_save_days(self, plan, text):
        lines = text.splitlines()
        day_pattern = re.compile(r'^Day\s*(\d+):\s*(.*)', re.IGNORECASE)

        current_day = None
        current_content = []

        for line in lines:
            match = day_pattern.match(line.strip())
            if match:
                if current_day is not None:
                    StudyDayPlan.objects.create(
                        study_plan=plan,
                        day=current_day,
                        content='\n'.join(current_content).strip(),
                        prompt_example='',
                        concept_summary=''
                    )
                current_day = int(match.group(1))
                current_content = [match.group(2)]
            elif current_day is not None:
                current_content.append(line)

        if current_day is not None:
            StudyDayPlan.objects.create(
                study_plan=plan,
                day=current_day,
                content='\n'.join(current_content).strip(),
                prompt_example='',
                concept_summary=''
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
        return StudyPlan.objects.filter(user=self.request.user).order_by('-created_at')
