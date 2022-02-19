from django.db import models

# Create your models here.
from GeoPress import settings

class OAuthUser(models.Model):
    author = models.ForeignKey(settings.dev.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='用户')
    openid = models.CharField(max_length=50)
    token = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.openid