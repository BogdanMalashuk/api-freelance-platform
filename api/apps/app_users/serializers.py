from rest_framework import serializers
from .models import User


class UserPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'login', 'role', 'password', 'phone', 'about', 'balance']


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'about']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'login', 'password', 'phone', 'about', 'balance', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            login=validated_data['login'],
            password=validated_data['password'],
            phone=validated_data.get('phone'),
            about=validated_data.get('about'),
            balance=validated_data.get('balance', 0.00),
            role=validated_data.get('role', User.Role.CLIENT)
        )
        if user.role == User.Role.ADMIN:
            user.is_staff = True

        user.save()
        return user
