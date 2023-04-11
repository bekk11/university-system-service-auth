from django.urls import path

from apps.main.student.api import CreateStudent, DeactivateStudent, DestroyStudent, \
    DetailStudent, ListStudent, RetrieveStudent, UpdateStudent, CreateStudentExel
from apps.main.student.api.update_avatar_student import UpdateAvatarStudent

urlpatterns = [
    path('list/', ListStudent.as_view()),

    path('create/', CreateStudent.as_view()),
    path('create-exel/', CreateStudentExel.as_view()),

    path('detail/<str:pk>/', DetailStudent.as_view()),
    path('retrieve/<str:pk>/', RetrieveStudent.as_view()),

    path('update/<str:pk>/', UpdateStudent.as_view()),
    path('update/avatar/<str:pk>/', UpdateAvatarStudent.as_view()),

    path('deactivate/<str:pk>/', DeactivateStudent.as_view()),
    path('destroy/<str:pk>/', DestroyStudent.as_view()),
]
