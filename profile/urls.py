from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfilesList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profile-create'),

]