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
    if User.objects.filter(username=data['username']).exists() or User.objects.filter(email=data['email']).exists():
        print('User with this name or email already exists')
        return Response({'detail': 'User with this name or email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        serializer = UserSerializer(data=request.data, many=False)
        if serializer.is_valid():
            user = User(
                first_name=data['name'],
                username=data['username'],
                email=data['email'],
                password=make_password(data['password']),
            )
            user.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        message = {'detail': e}
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
    if User.objects.filter(username=data['username']).exists() or User.objects.filter(email=data['email']).exists():
        print('User with this name or email already exists')
        return Response({'detail': 'User with this name or email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        serializer = UserSerializer(data=request.data, many=False)
        if serializer.is_valid():
            if 'password' in data and data['password'] != '':
                User.objects.filter(pk=request.user.pk).update(
                    password=make_password(data['password'])
                )

            User.objects.filter(pk=request.user.pk).update(
                username=data['username'],
                email=data['email'],
                first_name=data['name'],
                is_staff=data['is_staff']
            )
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e)
        return Response({"detail": 'Updating Failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_user(request, pk):
    data = request.data
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if 'password' in data and data['password'] != '':
                User.objects.filter(pk=pk).update(
                    password=make_password(data['password'])
                )

            User.objects.filter(pk=pk).update(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                is_staff=data['is_staff']
            )

            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()

    return Response({"detail": 'User deleted correctly'})






