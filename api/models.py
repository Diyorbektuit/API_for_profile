from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TgUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=123)
    tg_id = models.CharField(max_length=123, unique=True)
    username = models.CharField(max_length=123)
    tg_phone = models.CharField(max_length=123, unique=True)

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram'

    def __str__(self):
        return self.username

