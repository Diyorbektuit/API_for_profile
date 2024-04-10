from rest_framework import serializers
from .models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['user', 'username', 'tg_id', 'tg_phone', 'bio']

