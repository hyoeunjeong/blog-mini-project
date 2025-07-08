from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 프로필 소갯말
    bio = models.TextField(blank=True, null=True)

    # 프로필 이미지 추가
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.username
