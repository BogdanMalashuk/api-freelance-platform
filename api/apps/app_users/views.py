from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserPublicSerializer, UserPrivateSerializer, UserRegistrationSerializer
from ..app_users.permissions import IsOwner, IsAdminUser
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):  # post /api/users/register/
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserPrivateDetailView(generics.RetrieveAPIView):  # get /api/users/<id>/private/
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsOwner, IsAdminUser]


class UserPublicDetailView(generics.RetrieveAPIView):  # get /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [AllowAny]


class UserUpdateView(generics.UpdateAPIView):  # put, patch /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsOwner]


class UserListView(generics.ListAPIView):  # get /api/users/
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [IsAdminUser]
