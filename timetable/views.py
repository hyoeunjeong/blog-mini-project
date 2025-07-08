from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable
from .forms import TimetableForm
from django.contrib.auth.decorators import login_required
from django.db.models import F

@login_required
def timetable_view(request):
    timetable = Timetable.objects.filter(user=request.user).order_by('weekday', 'start_time')
    return render(request, 'timetable/timetable.html', {
        'timetable': timetable
    })

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

@login_required
def timetable_delete(request, pk):
    tt = get_object_or_404(Timetable, pk=pk, user=request.user)
    if request.method == 'POST':
        tt.delete()
        return redirect('timetable:view')
    return render(request, 'timetable/timetable_confirm_delete.html', {
        'item': tt
    })
