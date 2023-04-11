from django.urls import path

from apps.notification.api import NotificationsRetrieveAPIView, NotificationsDestroyAPIView, NotificationsUpdateAPIView, \
    NotificationsCreateAPIView, NotificationsListAPIView, NotificationsRecipientViewSet

urlpatterns = [
    path('list/', NotificationsListAPIView.as_view()),
    path('list/recipient/', NotificationsRecipientViewSet.as_view({'get': 'list'})),
    path('create/', NotificationsCreateAPIView.as_view()),

    path('retrieve/<int:pk>/', NotificationsRetrieveAPIView.as_view()),
    path('update/<int:pk>/', NotificationsUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', NotificationsDestroyAPIView.as_view()),
]
