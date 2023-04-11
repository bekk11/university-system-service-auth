from rest_framework.generics import CreateAPIView

from apps.group.serializers.group_serializer import GroupSerializer
from apps.group.models import Group
from user.permissions.admin_permission import AdminPermission


class GroupCreateAPIView(CreateAPIView):
    """
    This API is used to create new GROUP and must contain all required fields.
    """
    queryset = Group.objects.select_related('faculty').all()
    serializer_class = GroupSerializer
    permission_classes = [AdminPermission]

