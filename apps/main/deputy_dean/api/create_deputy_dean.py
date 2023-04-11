# Rest-Framework
from rest_framework.generics import CreateAPIView

# Project
from apps.main.deputy_dean.models import DeputyDean
from apps.main.deputy_dean.serializers.create_deputy_dean_serializer import DeputyDeanCreateSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeputyDeanCreateAPIView(CreateAPIView):
    queryset = DeputyDean.objects.select_related("user", "dean").all()
    serializer_class = DeputyDeanCreateSerializer
    permission_classes = [AdminPermission | DeanPermission]
