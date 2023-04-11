# Rest-Framework
from rest_framework.generics import UpdateAPIView

# Project
from apps.main.deputy_dean.models import DeputyDean
from apps.main.deputy_dean.serializers.update_deputy_dean_serializer import DeputyDeanUpdateSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeputyDeanUpdateAPIView(UpdateAPIView):
    queryset = DeputyDean.objects.select_related("user", "dean").all()
    serializer_class = DeputyDeanUpdateSerializer
    permission_classes = [AdminPermission | DeanPermission]
