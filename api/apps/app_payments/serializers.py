from rest_framework import serializers
from .models import Payment
from ..app_projects.models import Project


class PaymentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    sender = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'sender', 'amount', 'created_at', 'project']
        read_only_fields = ['id', 'sender', 'created_at']

    def create(self, validated_data):
        project = validated_data.get('project')
        if project.status == 'completed':
            raise serializers.ValidationError("Error. This project already completed.")

        request = self.context.get('request')
        creator = request.user

        if creator.balance < project.budget:
            raise serializers.ValidationError("Error. Not enough money for pauing.")

        validated_data['sender'] = creator

        project = validated_data.get('project')
        if project:
            project.status = 'completed'
            project.save()

        return super().create(validated_data)
