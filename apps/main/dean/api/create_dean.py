# Rest-Framework
from rest_framework.generics import CreateAPIView

# Project
from apps.main.dean.models import Dean
from apps.main.dean.serializers.create_dean_serializer import DeanCreateSerializer
from user.permissions.admin_permission import AdminPermission


class DeanCreateAPIView(CreateAPIView):
    """
    This API is used to create new DEAN and must contain all required fields.
    """
    queryset = Dean.objects.select_related('user').all()
    serializer_class = DeanCreateSerializer
    permission_classes = [AdminPermission]
