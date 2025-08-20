from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


# Using basic Serializer
class UserRegisterAPIViewSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user


class UserLoginAPIViewSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if (not username) or (not password):
            raise serializers.ValidationError("Missing username or password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("username or password was incorrect")

        data['user'] = user  # lấy user và trả về luôn sau khi validate, tránh query lại ở view
        return data


class TokenRefreshAPIViewSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=128)

    def validate(self, data):
        refresh_token = data.get('refresh_token')
        if not refresh_token:
            raise serializers.ValidationError("Refresh token is missing")
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = validated_data['password']
        return super().create(validated_data)