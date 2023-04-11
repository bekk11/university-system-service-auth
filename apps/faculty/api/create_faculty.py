from rest_framework.generics import CreateAPIView

from apps.faculty.serializers.faculty_serializer import FacultySerializer
from apps.faculty.models import Faculty
from user.permissions.admin_permission import AdminPermission


class FacultyCreateAPIView(CreateAPIView):
    """
    This API is used to create new FACULTY and must contain all required fields.
    """
    queryset = Faculty.objects.select_related('dean').all()
    serializer_class = FacultySerializer
    permission_classes = [AdminPermission]
