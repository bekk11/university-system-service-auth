from rest_framework.generics import ListAPIView

from user.models import User
from user.permissions.admin_permission import AdminPermission
from user.serializers.auth.custom_token_serializer import CustomStudentTokenSerializer


class UserListAPIView(ListAPIView):
    """
    This API is used to list entire User.
    """
    queryset = User.objects.all()
    serializer_class = CustomStudentTokenSerializer
    permission_classes = [AdminPermission]

