# Rest-Framework
from rest_framework.generics import RetrieveAPIView

# Project
from apps.main.dean.models import Dean
from apps.main.dean.serializers.dean_serializer import DeanSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeanRetrieveAPIView(RetrieveAPIView):
    """
    This API only lists one DEAN by id (pk).
    """
    queryset = Dean.objects.select_related('user').values('user_id',
                                                          'fullname',
                                                          'gender',
                                                          'profile_image')
    serializer_class = DeanSerializer
    permission_classes = [AdminPermission | DeanPermission]
