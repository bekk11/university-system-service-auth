from rest_framework.generics import ListAPIView

from apps.faculty.serializers.faculty_serializer import FacultySerializer
from apps.faculty.models import Faculty
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class FacultyListAPIView(ListAPIView):
    """
    This API is used to list entire FACULTY.
    """
    queryset = Faculty.objects.select_related('dean').all()
    serializer_class = FacultySerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]

    # User can search, filter by faculty name - 19-20 lines
    search_fields = ['name', ]
    filterset_fields = ['name', ]
