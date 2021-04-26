# Rest Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Models
from .models import Survey

# Serializers
from .serializers import SurveySerializer


class SurveyListAPIView(ListCreateAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    lookup_field = 'id'
