from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话号码')
    nickname = models.CharField(max_length=50, null=True, blank=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.jpg', max_length=100, verbose_name='用户头像')

    class Meta:
        # db_table = "userinfo"
        verbose_name = '用户中心'
        verbose_name_plural = verbose_name