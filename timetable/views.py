# 모듈과 클래스 import
from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable
from .forms import TimetableForm
from django.contrib.auth.decorators import login_required
  

# 시간표 목록 
# 로그인후 접근 가능  시간표 항목을 요일/ 시작 /시간 으로 나눔
def timetable_view(request):
    timetable = Timetable.objects.filter(user=request.user).order_by('weekday', 'start_time')
    return render(request, 'timetable/timetable.html', {
        'timetable': timetable
    })


# 시간표 추가 
# POST 요청이면 새 항목을 저장 GET 요청이면 빈거 
@login_required
def timetable_create(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            tt = form.save(commit=False)
            tt.user = request.user
            tt.save()
            return redirect('timetable:view')
    else:
        form = TimetableForm()
    return render(request, 'timetable/timetable_form.html', {
        'form': form,
        'title': '시간표 추가'
    })


# 시간표 수정 뷰
# 시간표 항목을 가져와서 수정 
@login_required
def timetable_edit(request, pk):
    tt = get_object_or_404(Timetable, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=tt)
        if form.is_valid():
            form.save()
            return redirect('timetable:view')
    else:
        form = TimetableForm(instance=tt)
    return render(request, 'timetable/timetable_form.html', {
        'form': form,
        'title': '시간표 수정'
    })


# 시간표 삭제 뷰
# 삭제 전 확인 페이지& POST 요청 삭제
@login_required
def timetable_delete(request, pk):
    tt = get_object_or_404(Timetable, pk=pk, user=request.user)
    if request.method == 'POST':
        tt.delete()
        return redirect('timetable:view')
    return render(request, 'timetable/timetable_confirm_delete.html', {
        'item': tt
    })
