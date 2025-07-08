from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.http import Http404

from .forms import CustomUserCreationForm, ProfileForm

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def profile_view(request):
    return render(request, 'account/profile_view.html', {
        'user_profile': request.user
    })


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile_view')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'account/profile_edit.html', {'form': form})



def public_profile_view(request, username):
    try:
        user_profile = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("존재하지 않는 사용자입니다.")

    return render(request, 'account/public_profile.html', {
        'user_profile': user_profile
    })
