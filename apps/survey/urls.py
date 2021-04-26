from django.conf.urls import url

# Views
from .views import SurveyListAPIView, SurveyDetailAPIView

urlpatterns = [
    url(r'^surveys/$', SurveyListAPIView.as_view(), name='surveys'),
    url(r'^surveys/(?P<id>[0-9a-f-]+)/$',
        SurveyDetailAPIView.as_view(), name='survey')
]
