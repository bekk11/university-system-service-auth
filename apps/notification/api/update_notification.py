from rest_framework.generics import UpdateAPIView

from apps.notification.serializers.update_notification_serializer import NotificationUpdateSerializer
from apps.notification.models import Notification
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class NotificationsUpdateAPIView(UpdateAPIView):
    """
    This API is used to update only ONE NOTIFICATION and must contain all required fields.
    """
    queryset = Notification.objects.select_related('from_user', 'blog').all()
    serializer_class = NotificationUpdateSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
