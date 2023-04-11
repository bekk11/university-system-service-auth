# Rest-Framework
from rest_framework.generics import UpdateAPIView

# Project
from apps.main.dean.models import Dean
from apps.main.dean.serializers.update_dean_serializer import DeanUpdateSerializer
from user.permissions.admin_permission import AdminPermission


class DeanUpdateAPIView(UpdateAPIView):
    """
    This API is used to update only ONE DEAN and must contain all required fields.
    """
    queryset = Dean.objects.select_related('user').all()
    serializer_class = DeanUpdateSerializer
    permission_classes = [AdminPermission]
