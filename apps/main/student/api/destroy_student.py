from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from apps.main.student.models import Student
from user.models import User
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class DestroyStudent(DestroyAPIView):
    """
    This API will delete student for forever
    """
    queryset = Student.objects.all()
    permission_classes = [AdminPermission | DeanPermission]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        glob_user = User.objects.get(id=instance.user.id)
        glob_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
