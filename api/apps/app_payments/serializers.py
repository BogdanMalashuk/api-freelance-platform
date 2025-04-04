from rest_framework import serializers
from .models import Payment
from ..app_projects.serializers import ProjectSerializer
from ..app_users.serializers import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'sender', 'amount', 'created_at', 'project']
