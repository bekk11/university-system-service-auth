# Rest-Framework
from rest_framework.generics import DestroyAPIView

# Project
from apps.main.dean.models import Dean
from apps.main.dean.serializers.dean_serializer import DeanSerializer
from user.permissions.admin_permission import AdminPermission


class DeanDestroyAPIView(DestroyAPIView):
    """
    This API is used to destroy existing DEAN.
    """
    queryset = Dean.objects.select_related('user').all()
    serializer_class = DeanSerializer
    permission_classes = [AdminPermission]
