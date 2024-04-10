from django.urls import path
from .views import tg_users_views
urlpatterns = [
    path('tg_users/', tg_users_views.TgUsersList.as_view(), name='tg-users-list'),
    path('tg_users/<int:pk>/', tg_users_views.TgUserDetail.as_view(), name='tg-users-detail'),
    path('tg_users/<int:pk>/update/', tg_users_views.TgUserUpdate.as_view(), name='tg-users-update'),
    path('tg_users/<int:pk>/delete/', tg_users_views.TgUserDelete.as_view(), name='tg-users-delete'),
    path('tg_users/create/', tg_users_views.TgUserCreate.as_view(), name='tg-users-create'),

]