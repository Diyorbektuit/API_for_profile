from api.serializers import TgUserSerializer
from api.models import TgUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class TgUsersList(ListAPIView):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = []


class TgUserDetail(RetrieveAPIView):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = []


class TgUserCreate(CreateAPIView):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = [IsAuthenticated]


class TgUserUpdate(UpdateAPIView):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permisiion_classes = [IsAuthenticated]


class TgUserDelete(DestroyAPIView):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permisiion_classes = [IsAuthenticated]
