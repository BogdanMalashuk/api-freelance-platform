from rest_framework import serializers
from .models import Project, Offer
from ..app_users.serializers import UserPrivateSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator = UserPrivateSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'budget', 'created_at', 'creator', 'status']


class OfferSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    freelancer = UserPrivateSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'project', 'freelancer', 'price', 'offer_details', 'created_at', 'status']
