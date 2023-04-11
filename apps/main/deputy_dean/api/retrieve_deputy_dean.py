# Rest-Framework
from rest_framework.generics import RetrieveAPIView

# Project
from apps.main.deputy_dean.models import DeputyDean
from apps.main.deputy_dean.serializers.deputy_dean_serializer import DeputyDeanSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeputyDeanRetrieveAPIView(RetrieveAPIView):
    queryset = DeputyDean.objects.select_related("user", "dean").values('id',
                                                                        'fullname',
                                                                        'gender',
                                                                        'profile_image',
                                                                        'user_id',
                                                                        'dean_id',
                                                                        'user__ROLE',
                                                                        'user__USER_ID')
    serializer_class = DeputyDeanSerializer
    permission_classes = [AdminPermission | DeanPermission]
