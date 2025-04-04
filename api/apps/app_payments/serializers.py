from rest_framework import serializers
from .models import Payments
from api.apps.app_users.serializers import UserSerializer
from api.apps.app_projects.serializers import ProjectSerializer


class PaymentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Payments
        fields = ['id', 'sender', 'amount', 'created_at', 'project']
