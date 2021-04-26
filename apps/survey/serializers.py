# Rest Framework
from rest_framework import serializers

# Models
from .models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'activity',
            'answers'
        ]
