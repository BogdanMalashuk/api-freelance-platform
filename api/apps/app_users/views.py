from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserPublicSerializer, UserPrivateSerializer, UserRegistrationSerializer
from ..app_users.permissions import IsAdminUser, IsAdminOrSelf, IsSelf
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):  # post /api/users/register/
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserPrivateDetailView(generics.RetrieveAPIView):  # get /api/users/<id>/private/
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsAdminOrSelf]


class UserPublicDetailView(generics.RetrieveAPIView):  # get /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [AllowAny]


class UserUpdateView(generics.UpdateAPIView):  # put, patch /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsSelf]


class UserListView(generics.ListAPIView):  # get /api/users/
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsAdminUser]


class UserDeleteView(generics.DestroyAPIView):  # delete /api/users/<id>/
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [IsAdminOrSelf]
