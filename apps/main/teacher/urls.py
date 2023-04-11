from django.urls import path

from apps.main.teacher.api.create_teacher import CreateTeacher
from apps.main.teacher.api.list_teacher import ListTeacher
from apps.main.teacher.api.public_info_teacher import PublicInfoTeacher
from apps.main.teacher.api.retrieve_teacher import RetrieveTeacher

urlpatterns = [
    path('list/', ListTeacher.as_view()),
    path('create/', CreateTeacher.as_view()),

    path('retrieve/<str:pk>/', RetrieveTeacher.as_view()),
    path('info/<str:pk>/', PublicInfoTeacher.as_view()),
]
