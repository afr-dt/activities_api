# Rest Framework
from rest_framework import serializers

# Models
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'property',
            'schedule',
            'title',
            'status'
        ]
