from django.urls import path
from .views import RegisterView, CustomTokenRefreshView, MyTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='registration'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]