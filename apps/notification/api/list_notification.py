from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.notification.models import Notification
from apps.notification.serializers.notifications_serializer import NotificationsSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission
from user.permissions.student_permission import StudentPermission


class NotificationsListAPIView(ListAPIView):
    """
    This API is used to list entire DEAN.
    """
    queryset = Notification.objects.select_related('from_user', 'blog').all()
    serializer_class = NotificationsSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission | StudentPermission]


class NotificationsRecipientViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Notification.objects.filter(blog__student__user=request.user)  # if app give error like excepted "pk" change request.user to request.user.pk
        serializer = NotificationsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AdminPermission | StudentPermission]
