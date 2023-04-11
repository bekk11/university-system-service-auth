from rest_framework.generics import DestroyAPIView

from apps.group.serializers.group_serializer import GroupSerializer
from apps.group.models import Group
from user.permissions.admin_permission import AdminPermission


class GroupDestroyAPIView(DestroyAPIView):
    """
    This API is used to destroy existing GROUP.
    """
    queryset = Group.objects.select_related('faculty').all()
    serializer_class = GroupSerializer
    permission_classes = [AdminPermission]


