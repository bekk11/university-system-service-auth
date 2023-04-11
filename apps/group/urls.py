from django.urls import path

from apps.group.api import GroupListAPIView, GroupCreateAPIView, GroupDestroyAPIView, GroupRetrieveAPIView, \
    GroupUpdateAPIView

urlpatterns = [
    path('list/', GroupListAPIView.as_view()),
    path('create/', GroupCreateAPIView.as_view()),

    path('retrieve/<int:pk>/', GroupRetrieveAPIView.as_view()),
    path('update/<int:pk>/', GroupUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', GroupDestroyAPIView.as_view()),
]
