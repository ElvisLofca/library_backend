from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueTogetherValidator


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'title': {'validators': []}
        }



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'is_staff', 'email']
        extra_kwargs = {
            'username': {'validators': []},
            'email': {'validators': []}
        }


class UserSerializerWithToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.first_name
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff

        return token


