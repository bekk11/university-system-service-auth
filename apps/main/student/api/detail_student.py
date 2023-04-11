from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from apps.main.student.models import Student
from apps.main.student.serializers.detail_student_serializer import StudentDetailSerializer
from user.permissions.student_permission import StudentPermission


class DetailStudent(RetrieveAPIView):
    """
    This API used to get all necessary data for putting private area for students.
    You should just send student id and take only necessary data for student
    This API is only for student. You can get data only if you have student permission
    """
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [StudentPermission]
