from django.urls import path

from apps.faculty.api import FacultyListAPIView, FacultyRetrieveAPIView, FacultyCreateAPIView, FacultyUpdateAPIView, \
    FacultyDestroyAPIView


urlpatterns = [
    path('list/', FacultyListAPIView.as_view()),
    path('create/', FacultyCreateAPIView.as_view()),

    path('retrieve/<int:pk>/', FacultyRetrieveAPIView.as_view()),
    path('update/<int:pk>/', FacultyUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', FacultyDestroyAPIView.as_view()),
]
