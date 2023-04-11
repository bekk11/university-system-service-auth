from rest_framework.generics import RetrieveAPIView

from apps.main.student.models import Student
from apps.main.student.serializers.list_student_serializer import StudentListSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class RetrieveStudent(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
