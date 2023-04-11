from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.main.teacher.models import Teacher
from apps.main.teacher.serializers.teacher_create_serializer import TeacherCreateSerializer


class CreateTeacher(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [AllowAny, ]  # this is temporary after testing it will be changed
