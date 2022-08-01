from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from base.serializers import UserSerializerWithToken, UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializerWithToken


@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        User.objects.create(
            first_name=data['name'],
            username=data['username'],
            email=data['email'],
            password=make_password(data['password']),
        )
        message = {'detail': 'User created successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    user = request.user
    users = User.objects.exclude(id=user.id)
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    data = request.data
    try:
        User.objects.filter(pk=request.user.pk).update(
            username=data['username'],
            email=data['email'],
            first_name=data['name'],
            is_staff=data['is_staff']
        )

        if 'password' in data and data['password'] != '':
            User.objects.filter(pk=request.user.pk).update(
                password=make_password(data['password'])
            )

    except Exception as e:
        print(e)
        return Response({"detail": 'Updating Failed'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(pk=request.user.pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_user(request, pk):
    data = request.data
    try:
        User.objects.filter(pk=pk).update(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            is_staff=data['is_staff']
        )

        if 'password' in data and data['password'] != '':
            User.objects.filter(pk=pk).update(
                password=make_password(data['password'])
            )

    except Exception as e:
        print(e)

    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()

    return Response({"detail": 'User deleted correctly'})






