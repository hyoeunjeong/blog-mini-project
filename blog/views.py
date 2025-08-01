from django.shortcuts import render, redirect, get_object_or_404  
from django.views import View  #
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.core.exceptions import PermissionDenied  
from django.db.models import Q  
from django.http import JsonResponse  
from django.utils.decorators import method_decorator  
from django.contrib.auth.decorators import login_required  
from django.views.decorators.http import require_POST 
import re  # 태그
from .models import Post, Comment, Tag  
from .forms import PostForm, CommentForm, HashTagForm  


# 글 목록 및 검색
class Index(View):
    def get(self, request):
        query = request.GET.get("q", "")
        posts = Post.objects.all().order_by('-created_at')

        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()

        return render(request, 'blog/post_list.html', {
            "posts": posts,
            "query": query,
            "title": "Blog"
        })


#글 작성
class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form, "title": "그력"})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            self.handle_tags(post)
            return redirect('blog:detail', pk=post.pk)
        return render(request, 'blog/post_form.html', {'form': form, "title": "그력"})

    def handle_tags(self, post):
        post.tags.clear()
        tags = set(re.findall(r'#(\w+)', post.content))
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)


#글 수정
class Update(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            raise PermissionDenied()
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {
            'form': form,
            'post': post,
            'title': '그 수정'
        })

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            raise PermissionDenied()
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            self.handle_tags(post)
            return redirect('blog:detail', pk=pk)
        return render(request, 'blog/post_form.html', {
            'form': form,
            'post': post,
            'title': '그 수정'
        })

    def handle_tags(self, post):
        post.tags.clear()
        tags = set(re.findall(r'#(\w+)', post.content))
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)


#글 삭제
class Delete(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_confirm_delete.html', {
            'post': post,
            'title': '그 삭제 확인'
        })

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            raise PermissionDenied()
        post.delete()
        return redirect('blog:post_list')


#글 상세 보기
class DetailView(View):
    def get(self, request, pk):
        try:
            post = Post.objects.prefetch_related('comments', 'tags').get(pk=pk)
        except Post.DoesNotExist:
            return render(request, '404.html', status=404)

        post.views += 1
        post.save(update_fields=['views'])

        return render(request, 'blog/post_detail.html', {
            "title": post.title,
            'post': post,
            'comments': post.comments.filter(parent__isnull=True),
            'tags': post.tags.all(),
            'comment_form': CommentForm(),
            'hashtag_form': HashTagForm(),
        })


#댓글 작성
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        parent_id = request.POST.get('parent')
        parent = Comment.objects.filter(pk=parent_id).first() if parent_id else None

        if form.is_valid():
            Comment.objects.create(
                post=post,
                content=form.cleaned_data['content'],
                writer=request.user,
                parent=parent,
            )
        return redirect('blog:detail', pk=pk)


# 댓글 삭제
class CommentDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.writer != request.user:
            raise PermissionDenied()
        post_id = comment.post.pk
        comment.delete()
        return redirect('blog:detail', pk=post_id)


#댓글 수정
class CommentEdit(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.writer != request.user:
            raise PermissionDenied()
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_edit.html', {
            'form': form,
            'comment': comment,
            'title': '댓글 수정'
        })

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.writer != request.user:
            raise PermissionDenied()
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', pk=comment.post.pk)
        return render(request, 'blog/comment_edit.html', {
            'form': form,
            'comment': comment,
            'title': '댓글 수정'
        })


#해시태그 추가
class HashTagWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = HashTagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data['name'].strip()
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return redirect('blog:detail', pk=pk)


#해시태그 삭제
class HashTagDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        for post in tag.post_set.all():
            post.tags.remove(tag)
        tag.delete()
        return redirect('blog:post_list')


#좋아요  
@method_decorator([login_required, require_POST], name='dispatch')
class ToggleLikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count(),
        })
