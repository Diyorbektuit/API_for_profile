from django.urls import path
from . import profile_views

urlpatterns = [
    path('profiles/', profile_views.ProfilesList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', profile_views.ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/update/', profile_views.ProfileUpdate.as_view(), name='profile-update'),
    path('profiles/<int:pk>/delete/', profile_views.ProfileDelete.as_view(), name='profile-delete'),
    path('profiles/create/', profile_views.ProfileCreate.as_view(), name='profile-create'),

]