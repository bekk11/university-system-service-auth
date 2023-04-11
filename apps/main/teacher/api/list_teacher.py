from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.main.teacher.models import Teacher
from apps.main.teacher.serializers.teacher_serializer import TeacherSerializer


class ListTeacher(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]  # this is temporary after testing it will be changed
