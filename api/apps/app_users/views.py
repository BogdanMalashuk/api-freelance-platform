from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from ..app_users.permissions import IsOwner, IsAdminUser
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):  # post /api/users/register/
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveAPIView):  # get /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserUpdateView(generics.UpdateAPIView):  # put, patch /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserListView(generics.ListAPIView):  # get /api/users/
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
