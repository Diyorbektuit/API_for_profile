from django.contrib import admin
from .models import Posts
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')
    search_filter = ('title',)


admin.site.register(Posts, PostsAdmin)