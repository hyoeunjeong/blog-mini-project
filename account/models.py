# account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 필요 시 사용자 프로필 필드 추가 가능
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
