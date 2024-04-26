from profile.serializers import ProfileSerializer
from profile.models import Profile
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


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
    permission_classes = []


class ProfileUpdate(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permisiion_classes = [IsAdminUser]


class ProfileDelete(DestroyAPIView):
    permisiion_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

