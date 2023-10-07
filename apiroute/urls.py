from rest_framework import routers
from django.urls import path, include
from .views import ETFListAPIView, protected_view


urlpatterns = [
    path("test/", protected_view, name='test-view'),
    path("", ETFListAPIView.as_view()),
]
