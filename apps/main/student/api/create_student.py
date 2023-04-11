from rest_framework.generics import CreateAPIView

from apps.main.student.models import Student
from apps.main.student.serializers.student_create_update_serializer import StudentCreateUpdateSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class CreateStudent(CreateAPIView):
    """
    This API is used to create new student
    """
    queryset = Student.objects.all()
    serializer_class = StudentCreateUpdateSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
