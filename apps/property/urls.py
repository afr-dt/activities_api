from django.conf.urls import url

# Views
from .views import PropertyListAPIView, PropertyDetailAPIView

urlpatterns = [
    url(r'^properties/$', PropertyListAPIView.as_view(), name='properties'),
    url(r'^properties/(?P<id>[0-9a-f-]+)/$',
        PropertyDetailAPIView.as_view(), name='property')
]
