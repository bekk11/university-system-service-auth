from rest_framework.generics import RetrieveAPIView

from apps.main.teacher.models import Teacher
from apps.main.teacher.serializers.teacher_public_info_serializer import TeacherPublicInfoSerializer


class PublicInfoTeacher(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherPublicInfoSerializer
