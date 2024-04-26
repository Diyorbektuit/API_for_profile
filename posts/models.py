from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=123)
    body = models.TextField()
    img = models.ImageField(upload_to='posts_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title