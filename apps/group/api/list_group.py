from rest_framework.generics import ListAPIView

from apps.group.models import Group
from apps.group.serializers.group_serializer import GroupSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class GroupListAPIView(ListAPIView):
    """
    This API is used to list entire GROUP.
    """
    queryset = Group.objects.select_related('faculty', 'faculty__dean').all()
    serializer_class = GroupSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]

    # User can filter by group name and faculty name - 19 lines
    filterset_fields = ['name', 'faculty', ]
