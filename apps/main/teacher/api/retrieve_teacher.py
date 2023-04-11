from rest_framework.generics import RetrieveAPIView

from apps.main.teacher.models import Teacher
from apps.main.teacher.serializers.teacher_serializer import TeacherSerializer


class RetrieveTeacher(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
