# Django
from django.urls import path

# Project
from apps.main.dean.api import DeanCreateAPIView, DeanUpdateAPIView, DeanRetrieveAPIView, DeanListAPIView, \
    DeanDestroyAPIView

urlpatterns = [
    path("create/", DeanCreateAPIView.as_view()),
    path("list/", DeanListAPIView.as_view()),
    path("update/<int:pk>/", DeanUpdateAPIView.as_view()),
    path("retrieve/<int:pk>/", DeanRetrieveAPIView.as_view()),
    path("destroy/<int:pk>/", DeanDestroyAPIView.as_view()),
]
