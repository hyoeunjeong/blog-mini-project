from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.http import Http404

from .forms import CustomUserCreationForm, ProfileForm

User = get_user_model()

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'account/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        return context
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'account/profile_edit.html'
    success_url = reverse_lazy('account:profile_view')

    def get_object(self):
        return self.request.user
class PublicProfileView(View):
    def get(self, request, username):
        user_profile = get_object_or_404(User, username=username)
        return render(request, 'account/public_profile.html', {
            'user_profile': user_profile
        })
