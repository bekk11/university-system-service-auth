from rest_framework.generics import DestroyAPIView

from apps.notification.serializers.notifications_serializer import NotificationsSerializer
from apps.notification.models import Notification
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class NotificationsDestroyAPIView(DestroyAPIView):
    """
    This API is used to destroy existing NOTIFICATIONS.
    """
    queryset = Notification.objects.select_related('from_user', 'blog').all()
    serializer_class = NotificationsSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
