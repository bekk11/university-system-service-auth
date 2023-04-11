from rest_framework.generics import RetrieveAPIView

from apps.notification.models import Notification
from apps.notification.serializers.notifications_serializer import NotificationsSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission
from user.permissions.student_permission import StudentPermission


class NotificationsRetrieveAPIView(RetrieveAPIView):
    """
    This API only lists one NOTIFICATION by id (pk).
    """
    queryset = Notification.objects.select_related('from_user', 'blog').all()
    serializer_class = NotificationsSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission | StudentPermission]
