# Rest Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Models
from .models import Activity

# Serializers
from .serializers import ActivitySerializer


class ActivityListAPIView(ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ActivityDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    lookup_field = 'id'
