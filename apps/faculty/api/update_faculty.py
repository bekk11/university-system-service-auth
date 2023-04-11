from rest_framework.generics import UpdateAPIView

from apps.faculty.serializers.faculty_serializer import FacultySerializer
from apps.faculty.models import Faculty
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class FacultyUpdateAPIView(UpdateAPIView):
    """
    This API is used to update only ONE FACULTY and must contain all required fields.
    """
    queryset = Faculty.objects.select_related('dean').all()
    serializer_class = FacultySerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]