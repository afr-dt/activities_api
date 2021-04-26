# Rest Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Models
from .models import Property

# Serializers
from .serializers import PropertySerializer


class PropertyListAPIView(ListCreateAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class PropertyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    lookup_field = 'id'
