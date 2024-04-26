from django.urls import path
from .views import DeletePostView, ListPostsView, DetailPostView, PostCreateView, UpdatePostView
urlpatterns = [
    path('posts/', ListPostsView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),

]