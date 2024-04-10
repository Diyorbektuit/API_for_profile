from django.contrib import admin
from .models import TgUser
# Register your models here.


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'username']

