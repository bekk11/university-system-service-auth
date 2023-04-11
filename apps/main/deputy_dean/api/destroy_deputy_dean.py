# Rest-Framework
from rest_framework.generics import DestroyAPIView

# Project
from apps.main.deputy_dean.models import DeputyDean
from apps.main.deputy_dean.serializers.deputy_dean_serializer import DeputyDeanSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeputyDeanDestroyAPIView(DestroyAPIView):
    queryset = DeputyDean.objects.select_related("user", "dean").all()
    serializer_class = DeputyDeanSerializer
    permission_classes = [AdminPermission | DeanPermission]
