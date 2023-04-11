from rest_framework.generics import UpdateAPIView

from apps.main.student.models import Student
from apps.main.student.serializers.student_create_update_serializer import StudentCreateUpdateSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission
from user.permissions.student_permission import StudentPermission


class UpdateStudent(UpdateAPIView):
    """
    This API is for editing user info You should send only PATCH request because this table has image field if you
    update only texts then image field will be null
    """
    queryset = Student.objects.all()
    serializer_class = StudentCreateUpdateSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission | StudentPermission]
