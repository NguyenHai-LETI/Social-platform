from tokenize import TokenError
import logging

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema
from drf_spectacular.extensions import OpenApiAuthenticationExtension

from .serializers import (
    UserRegisterAPIViewSerializer,
    UserLoginAPIViewSerializer,
    TokenRefreshAPIViewSerializer,
    RegisterSerializer
)

logger = logging.getLogger('myapp')
# Define 2 methods for register-login: using APIView and using genericsView/others built-in view with serializers support
# 1. Using APIView
class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=UserRegisterAPIViewSerializer,
        summary="Đăng ký người dùng",
        description="API này cho phép người dùng đăng ký tài khoản mới",
        tags=['Using APIView'],
    )
    def post(self, request):
        serializer = UserRegisterAPIViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Tạo user -> gọi tới create()
        user = serializer.save()
        logger.info(f"Successfully register with username: {user.username}")

        response_data = {
            "message": "Đăng ký thành công. Vui lòng login để lấy token.",
            "user_id": user.id,
            "username": user.username
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    # APIView không tự động tạo tài liệu API trên swagger UI, cần sử dụng decorator khai báo
    @extend_schema(
        # Chỉ định serializer cho dữ liệu đầu vào của phương thức POST
        request=UserLoginAPIViewSerializer,
        summary="Đăng nhập người dùng",
        description="API này cho phép người dùng đăng nhập để lấy token xác thực.",
        tags=['Using APIView'],
    )
    def post(self, request):
        serializer = UserLoginAPIViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # valid_field and object in UserLoginAPIViewSerializer

        user = serializer.validated_data['user']  # user đã validate trong serializers

        # Tạo token và refresh token sử dụng simple JWT
        refresh = RefreshToken.for_user(user)  # tạo token với unique ID, nếu bật blackList được lưu lại trong OutStandingToken
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Ghi log thành công khi login
        logger.info(f"User {user.username} logged in successfully")

        response_data = {
            "message": "Đăng nhập thành công. Sử dụng serializers",
            "token": access_token,
            "refresh_token": refresh_token,
            "user_id": user.id,
            "username": user.username
        }
        return Response(response_data, status=status.HTTP_200_OK)


class TokenRefreshAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=TokenRefreshAPIViewSerializer,
        summary="Refresh token",
        description="This API take new access token and refresh token, put former refresh token to blackList",
        tags=['Using APIView'],
    )
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            # validate refresh_token và tạo refresh token mới, thêm refresh_token cũ vào blackList neu da setting
            refresh = RefreshToken(refresh_token)
            # tạo access_token mới
            access_token = str(refresh.access_token)
            logger.info(f"Successfully refresh token!")

            response_data = {
                'message': 'Lấy access token và refresh token mới thành công',
                'access_token': access_token,
                'token': access_token
            }
            return Response(response_data)

        except TokenError as e:
            raise InvalidToken({'detail': 'Refresh token error or blacklisted'})


class ProtectedAPIView(APIView):
    # DRF tự động validate token
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        summary="Protected API",
        description="Test API need authentication",
        tags=['Using APIView']
    )
    def get(self, request):
        user = request.user  # request.user là người dùng đã được xác thực

        response_data = {
            "message": 'Lấy thông tin thành công',
            "username": user.username,
            "email": user.email,
        }
        return Response(response_data, status=status.HTTP_200_OK)


# 2. Using genericView/other built-in view
class RegisterGenericView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    


class LoginGenericView():
    pass

