from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterAPIView,
    LoginAPIView,
    UserListView,
    TokenRefreshAPIView,
    RegisterGenericView
)


urlpatterns = [
    # API using APIView
    path('api-view/register/', RegisterAPIView.as_view(), name='register_api'),
    path('api-view/login/', LoginAPIView.as_view(), name='login_api'),
    path('api-view/token/refresh', TokenRefreshAPIView.as_view(), name='profile'),
    path('api-view/list/', UserListView.as_view(), name='users_list_api'),

    #API using GenericAPIView
    path('register/', RegisterGenericView.as_view(), name='register_generic'),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Đường dẫn để làm mới access token khi nó hết hạn
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]