from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
import re

from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm, HashTagForm

# ======================
# Post Views
# ======================

class Index(View):
    def get(self, request):
        query = request.GET.get("q", "")
        posts = Post.objects.all().order_by('-created_at')

        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()

        return render(request, 'blog/post_list.html', {
            "posts": posts,
            "query": query,
            "title": "Blog"
        })


class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {
            'form': form,
            "title": "글 작성"
        })

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            self.handle_tags(post)
            return redirect('blog:detail', pk=post.pk)
        return render(request, 'blog/post_form.html', {
            'form': form,
            "title": "글 작성"
        })

    def handle_tags(self, post):
        post.tags.clear()
        tags = set(re.findall(r'#(\w+)', post.content))
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)


class Update(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            raise PermissionDenied()
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {
            'form': form,
            'post': post,
            'title': '글 수정'
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
            'title': '글 수정'
        })

    def handle_tags(self, post):
        post.tags.clear()
        tags = set(re.findall(r'#(\w+)', post.content))
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)


class Delete(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_confirm_delete.html', {
            'post': post,
            'title': '글 삭제 확인'
        })

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            raise PermissionDenied()
        post.delete()
        return redirect('blog:post_list')


class DetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post.objects.prefetch_related('comments', 'tags'), pk=pk)
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


# ======================
# Comment Views
# ======================

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


class CommentDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.writer != request.user:
            raise PermissionDenied()
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)


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


# ======================
# HashTag Views
# ======================

class HashTagWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = HashTagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data['name'].strip()
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return redirect('blog:detail', pk=pk)


class HashTagDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        for post in tag.post_set.all():
            post.tags.remove(tag)
        tag.delete()
        return redirect('blog:post_list')
