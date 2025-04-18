from rest_framework import serializers
from .models import Project, Offer
from ..app_users.serializers import UserPrivateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.id')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'budget', 'created_at', 'creator', 'status', 'executor']


class OfferSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    freelancer = UserPrivateSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'project', 'freelancer', 'offer_details', 'created_at', 'status']
