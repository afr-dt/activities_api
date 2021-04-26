# Rest Framework
from rest_framework import serializers

# Models
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'address',
            'description',
            'status'
        ]
