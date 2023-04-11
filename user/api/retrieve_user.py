from rest_framework.generics import RetrieveAPIView

from user.models import User
from user.permissions.admin_permission import AdminPermission
from user.serializers.auth.custom_token_serializer import CustomStudentTokenSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """
    This API only lists one USER by id (pk).
    """
    queryset = User.objects.all()
    serializer_class = CustomStudentTokenSerializer
    permission_classes = [AdminPermission]

