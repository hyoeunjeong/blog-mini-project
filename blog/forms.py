from django import forms
from .models import Post, Comment


# 게시글 작성/수정 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  
        fields = ['title', 'content', 'image'] 

      
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'  
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',  
                'rows': 10  
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'  
            }),
        }


#댓글 작성/수정 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        fields = ['content']  

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3  
            }),
        }


#해시태그 입력 폼
class HashTagForm(forms.Form):
    name = forms.CharField(
        label='태그 이름',       
        max_length=10,           
        widget=forms.TextInput(attrs={
            'class': 'form-control' 
        })
    )
