from rest_framework.generics import DestroyAPIView

from apps.faculty.serializers.faculty_serializer import FacultySerializer
from apps.faculty.models import Faculty
from user.permissions.admin_permission import AdminPermission


class FacultyDestroyAPIView(DestroyAPIView):
    """
    This API is used to destroy existing FACULTY.
    """
    queryset = Faculty.objects.select_related('dean').all()
    serializer_class = FacultySerializer
    permission_classes = [AdminPermission]