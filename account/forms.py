from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['bio', 'profile_image']  
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': '자기소개를 입력하세요...'
            }),
        }
