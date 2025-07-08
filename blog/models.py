from django.db import models
from django.conf import settings
from django.urls import reverse


#게시글 분류용
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  

    class Meta:
        ordering = ['name']  
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리들'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_page', args=[self.slug])


# 게시글에 붙는 태그 
class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)  

    class Meta:
        ordering = ['name']
        verbose_name = '태그'
        verbose_name_plural = '태그들'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:search', args=[self.name])


#블로그 게시글(Post) 
class Post(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField()  
    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  
    views = models.PositiveIntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  
    tags = models.ManyToManyField(Tag, blank=True)  

    likes = models.ManyToManyField(  
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True
    )

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = '포스트'
        verbose_name_plural = '포스트들'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.pk)])



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    parent = models.ForeignKey(  
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    class Meta:
        ordering = ['created_at']  
        verbose_name = '댓글'
        verbose_name_plural = '댓글들'

    def __str__(self):
        return f'{self.writer} on {self.post.title}'
