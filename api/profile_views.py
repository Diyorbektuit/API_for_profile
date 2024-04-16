from api.serializers import ProfileSerializer
from api.models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView


class ProfilesList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []


class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []


class ProfileCreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileUpdate(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permisiion_classes = [IsAuthenticated]


class ProfileDelete(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permisiion_classes = [IsAuthenticated]
