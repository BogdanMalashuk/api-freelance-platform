from rest_framework import serializers
from .models import Payments
from project.app_users.serializers import UserSerializer
from project.app_projects.serializers import ProjectSerializer


class PaymentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Payments
        fields = ['id', 'sender', 'amount', 'created_at', 'project']
