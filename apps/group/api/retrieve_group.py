from rest_framework.generics import RetrieveAPIView

from apps.group.serializers.group_serializer import GroupSerializer
from apps.group.models import Group
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class GroupRetrieveAPIView(RetrieveAPIView):
    """
    This API only lists one GROUP by id (pk).
    """
    queryset = Group.objects.select_related('faculty', 'faculty__dean').all()
    serializer_class = GroupSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]



