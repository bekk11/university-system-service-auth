# Django
from django.urls import path

# Project
from apps.main.deputy_dean.api import DeputyDeanCreateAPIView, DeputyDeanUpdateAPIView, DeputyDeanListAPIView, \
    DeputyDeanRetrieveAPIView, DeputyDeanDestroyAPIView

urlpatterns = [
    path("create/", DeputyDeanCreateAPIView.as_view()),
    path("list/", DeputyDeanListAPIView.as_view()),
    path("update/<int:pk>/", DeputyDeanUpdateAPIView.as_view()),
    path("retrieve/<int:pk>/", DeputyDeanRetrieveAPIView.as_view()),
    path("destroy/<int:pk>/", DeputyDeanDestroyAPIView.as_view())
]

