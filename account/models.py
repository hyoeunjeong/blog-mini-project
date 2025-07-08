from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField("프로필 소개", blank=True, null=True)
    profile_image = models.ImageField(
        "프로필 이미지",
        upload_to='profile/', 
        blank=True,
        null=True
    )
    def __str__(self):
        return self.username
