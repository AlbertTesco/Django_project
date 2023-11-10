from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None  # Т.к. делаем авторизацию по email

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    verified = models.BooleanField(default=False, verbose_name='Активация')
    verification_code = models.CharField(default=0, verbose_name='Код верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
