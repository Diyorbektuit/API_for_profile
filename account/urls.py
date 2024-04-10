from django.urls import path
from .views import RegisterView, CustomTokenRefreshView, MyTokenObtainPairView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='registration'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]