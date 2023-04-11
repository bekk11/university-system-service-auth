from rest_framework.generics import UpdateAPIView

from apps.group.serializers.group_serializer import GroupSerializer
from apps.group.models import Group
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class GroupUpdateAPIView(UpdateAPIView):
    """
    This API is used to update only ONE GROUP and must contain all required fields.
    """
    queryset = Group.objects.select_related('faculty').all()
    serializer_class = GroupSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]



