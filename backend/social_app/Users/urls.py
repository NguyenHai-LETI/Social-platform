from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterAPIView,
    LoginAPIView,
    ProtectedAPIView,
    TokenRefreshAPIView
)


urlpatterns = [
    # API using APIView
    path('apiview/register/', RegisterAPIView.as_view(), name='register_api'),
    path('apiview/login/', LoginAPIView.as_view(), name='login_api'),
    path('apiview/token/refresh', TokenRefreshAPIView.as_view(), name='profile'),
    path('apiview/protected/', ProtectedAPIView.as_view(), name='protected_api'),


    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Đường dẫn để làm mới access token khi nó hết hạn
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]