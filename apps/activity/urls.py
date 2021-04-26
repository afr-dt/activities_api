from django.conf.urls import url

# Views
from .views import ActivityListAPIView, ActivityDetailAPIView

urlpatterns = [
    url(r'^activities/$', ActivityListAPIView.as_view(), name='activities'),
    url(r'^activities/(?P<id>[0-9a-f-]+)/$',
        ActivityDetailAPIView.as_view(), name='activity')
]
